"""Execute tutorial notebooks with writable runtime directories.

This helper keeps environment repair out of learner-facing notebooks. It runs
``jupyter nbconvert --execute`` with temporary ``HOME``, ``XDG_CACHE_HOME``,
``IPYTHONDIR``, and ``MPLCONFIGDIR`` directories, then checks the executed
notebook for stored errors, stderr streams, tracebacks, warning lines, and
broken local links.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Iterable
from urllib.parse import unquote

import nbformat

INLINE_LINK_RE = re.compile(r"(?<!!)\[[^\]]+\]\(([^)]+)\)")
REFERENCE_LINK_RE = re.compile(r"^\[[^\]]+\]:\s*(\S+)", re.MULTILINE)
WARNING_RE = re.compile(r"(^|: )([A-Za-z]*Warning):")
KERNEL_TCP_WARNING_RE = re.compile(
    r"^\[IPKernelApp\] WARNING \| Kernel is running over TCP without encryption\."
)


def output_name_for(notebook_path: Path) -> str:
    """Return a collision-resistant output filename for a notebook path."""
    resolved = notebook_path.resolve()
    try:
        parts = resolved.relative_to(Path.cwd().resolve()).parts
    except ValueError:
        parts = resolved.parts[1:]
    stem = "__".join(parts)[: -len(".ipynb")]
    return f"{stem}.executed.ipynb"


def notebook_text(output: nbformat.NotebookNode) -> str:
    if "text" in output:
        text = output["text"]
        return "".join(text) if isinstance(text, list) else str(text)
    data = output.get("data", {})
    if "text/plain" in data:
        text = data["text/plain"]
        return "".join(text) if isinstance(text, list) else str(text)
    return ""


def clean_nbconvert_output(text: str) -> str:
    """Remove runner-only noise while preserving real notebook validation."""
    lines = [
        line for line in text.splitlines() if not KERNEL_TCP_WARNING_RE.search(line)
    ]
    if not lines:
        return ""
    return "\n".join(lines) + "\n"


def local_link_targets(source: str) -> Iterable[str]:
    yield from INLINE_LINK_RE.findall(source)
    yield from REFERENCE_LINK_RE.findall(source)


def validate_executed_notebook(notebook_path: Path, link_base_dir: Path) -> list[str]:
    """Return validation problems found in an executed notebook."""
    notebook = nbformat.read(notebook_path, as_version=4)
    problems: list[str] = []

    for cell_index, cell in enumerate(notebook.cells, start=1):
        if cell.cell_type == "code":
            for output in cell.get("outputs", []):
                output_type = output.get("output_type")
                if output_type == "error":
                    ename = output.get("ename", "<unknown>")
                    evalue = output.get("evalue", "")
                    problems.append(
                        f"cell {cell_index}: error output: {ename}: {evalue}"
                    )
                    continue

                if output_type == "stream" and output.get("name") == "stderr":
                    text = notebook_text(output).strip().splitlines()
                    first_line = text[0] if text else "<empty stderr>"
                    problems.append(f"cell {cell_index}: stderr output: {first_line}")
                    continue

                text = notebook_text(output)
                if "Traceback (most recent call last)" in text:
                    problems.append(f"cell {cell_index}: traceback text in output")
                for line in text.splitlines():
                    stripped = line.strip()
                    if WARNING_RE.search(stripped) or stripped.startswith("WARNING:"):
                        problems.append(
                            f"cell {cell_index}: warning output: {stripped}"
                        )

        if cell.cell_type == "markdown":
            for raw_target in local_link_targets(cell.source):
                target = unquote(raw_target.strip())
                if not target or target.startswith(("http:", "https:", "mailto:", "#")):
                    continue
                target_path = target.split("#", 1)[0]
                if not target_path:
                    continue
                resolved = (link_base_dir / target_path).resolve()
                if not resolved.exists():
                    problems.append(f"cell {cell_index}: broken local link {target!r}")

    return problems


def runtime_environment(
    parent_env: dict[str, str], runtime_dir: Path
) -> dict[str, str]:
    env = parent_env.copy()
    home_dir = runtime_dir / "home"
    cache_dir = runtime_dir / "cache"
    ipython_dir = runtime_dir / "ipython"
    matplotlib_config_dir = runtime_dir / "matplotlib"
    jupyter_runtime_dir = runtime_dir / "jupyter_runtime"
    jupyter_config_dir = runtime_dir / "jupyter_config"
    jupyter_data_dir = runtime_dir / "jupyter_data"
    for directory in [
        home_dir,
        cache_dir,
        ipython_dir,
        matplotlib_config_dir,
        jupyter_runtime_dir,
        jupyter_config_dir,
        jupyter_data_dir,
    ]:
        directory.mkdir(parents=True, exist_ok=True)
    env.update(
        {
            "HOME": str(home_dir),
            "XDG_CACHE_HOME": str(cache_dir),
            "IPYTHONDIR": str(ipython_dir),
            "MPLCONFIGDIR": str(matplotlib_config_dir),
            "JUPYTER_RUNTIME_DIR": str(jupyter_runtime_dir),
            "JUPYTER_CONFIG_DIR": str(jupyter_config_dir),
            "JUPYTER_DATA_DIR": str(jupyter_data_dir),
        }
    )
    return env


def execute_notebook(
    notebook_path: Path, output_dir: Path | None, inplace: bool
) -> Path:
    if not notebook_path.is_file():
        raise FileNotFoundError(f"Notebook does not exist: {notebook_path}")
    if notebook_path.suffix != ".ipynb":
        raise ValueError(f"Expected a .ipynb notebook path: {notebook_path}")

    with tempfile.TemporaryDirectory(prefix="nrpy_notebook_runtime_") as tmp_dir:
        env = runtime_environment(os.environ, Path(tmp_dir))
        cmd = [
            sys.executable,
            "-m",
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
        ]
        if inplace:
            cmd.append("--inplace")
            executed_path = notebook_path
        else:
            assert output_dir is not None
            output_dir.mkdir(parents=True, exist_ok=True)
            executed_path = output_dir / output_name_for(notebook_path)
            cmd.extend(
                ["--output-dir", str(output_dir), "--output", executed_path.name]
            )
        cmd.append(str(notebook_path))

        result = subprocess.run(
            cmd,
            cwd=Path.cwd(),
            env=env,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            check=False,
        )
        if result.returncode != 0:
            print(clean_nbconvert_output(result.stdout), end="")
            raise RuntimeError(f"Notebook execution failed: {notebook_path}")
        if result.stdout:
            print(clean_nbconvert_output(result.stdout), end="")

    return executed_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Execute tutorial notebooks with writable temporary runtime dirs."
    )
    parser.add_argument(
        "--inplace",
        action="store_true",
        help="Refresh outputs in the input notebooks instead of writing copies.",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        help="Directory for executed notebook copies. Incompatible with --inplace.",
    )
    parser.add_argument("notebooks", nargs="+", type=Path, help="Notebook paths.")
    args = parser.parse_args()
    if args.inplace and args.output_dir is not None:
        parser.error("--output-dir cannot be used with --inplace")
    return args


def main() -> int:
    args = parse_args()
    output_dir = args.output_dir
    if not args.inplace and output_dir is None:
        output_dir = Path(tempfile.mkdtemp(prefix="nrpy_notebook_outputs_"))
        print(f"executed notebook output directory: {output_dir}")

    failures: list[str] = []
    for notebook_path in args.notebooks:
        try:
            executed_path = execute_notebook(notebook_path, output_dir, args.inplace)
            problems = validate_executed_notebook(
                executed_path, notebook_path.parent.resolve()
            )
            if problems:
                failures.append(f"{executed_path}:")
                failures.extend(f"  - {problem}" for problem in problems)
            else:
                print(f"validated: {executed_path}")
        except Exception as exc:  # noqa: BLE001 - CLI should report all notebooks.
            failures.append(f"{notebook_path}: {exc}")

    if failures:
        print("notebook validation failed:", file=sys.stderr)
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
