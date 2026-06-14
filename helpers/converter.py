"""Convert notebooks to and from this repository's percent-script format.

The "percent" format handled here is a small, lossy, line-oriented subset of
the Jupyter/Jupytext-style percent script convention. Its exact behavior is
defined by this file:

- Files are read and written as UTF-8 text. Line endings are normalized to
  ``"\n"`` when written.
- A physical script line is a cell marker when its first four characters are
  exactly ``# %%``. Marker detection is global: it happens before code or
  markdown cell content is interpreted, so any physical line beginning with
  ``# %%`` starts a new cell.
- A marker line containing the case-sensitive substring ``[markdown]`` anywhere
  in the line creates a markdown cell. Every other marker line creates a code
  cell. Other marker text is not preserved.
- Lines before the first marker are discarded when converting a script to a
  notebook. A script with no marker becomes an empty notebook.
- Code cell content is all text from the line after a code marker up to, but
  not including, the next marker. The lines are joined with ``"\n"`` and
  ``rstrip()`` is applied to the cell source, so trailing blank lines and
  trailing whitespace at the end of the cell are lost.
- A literal code line that starts in column 0 with ``# %%`` cannot be
  represented directly in this format because it is always parsed as the next
  cell marker.
- Markdown cell content is all text from the line after a markdown marker up
  to, but not including, the next marker. Each markdown line is decoded as:

  - ``# `` followed by text: remove exactly the first two characters. This is
    what notebook-to-script conversion emits for nonblank markdown lines.
  - ``#`` followed by anything else: remove the leading ``#`` and then strip
    remaining leading whitespace. A bare ``#`` therefore encodes a blank
    markdown line.
  - Any non-``#`` line: keep it verbatim.

  The decoded markdown lines are joined with ``"\n"`` and ``rstrip()`` is
  applied to the cell source, so trailing blank lines and trailing whitespace at
  the end of the cell are lost. To encode markdown text whose decoded content
  begins with ``# %%``, prefix it as normal markdown content; for example,
  ``# # %% not a marker`` decodes to ``# %% not a marker``.
- Notebook-to-script conversion emits only code and markdown cells. Unsupported
  cell types are skipped and reported on stdout. Outputs, execution counts,
  notebook metadata, and cell metadata are not serialized into the percent file.
- Script-to-notebook conversion creates a bare nbformat v4 notebook containing
  only code and markdown cells.
- Successful conversions print ``source -> destination`` on stdout.

Minimal example:

    # %% [markdown]
    # # Title
    #
    # Markdown text.
    # %%
    print("hello")
"""

import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell
from pathlib import Path


def ipynb_to_percent_script(ipynb_path, script_path):
    """
    Convert a .ipynb with only code + markdown cells
    into a .py file using # %% / # %% [markdown] markers.
    """
    ipynb_path = Path(ipynb_path)
    script_path = Path(script_path)

    nb = nbformat.read(ipynb_path, as_version=4)

    lines = []

    for cell in nb.cells:
        if cell.cell_type == "markdown":
            lines.append("# %% [markdown]")
            for line in cell.source.splitlines():
                if line.strip() == "":
                    lines.append("#")
                else:
                    lines.append("# " + line)
            lines.append("")

        elif cell.cell_type == "code":
            lines.append("# %%")
            if cell.source:
                lines.extend(cell.source.splitlines())
            lines.append("")

        else:
            # Only handling code + markdown; skip anything else
            print(f"Skipping unsupported cell type: {cell.cell_type!r}")

    script_text = "\n".join(lines).rstrip() + "\n"
    script_path.write_text(script_text, encoding="utf-8")
    print(f"{ipynb_path} -> {script_path}")


def percent_script_to_ipynb(script_path, ipynb_path):
    """
    Convert a # %% / # %% [markdown] .py file back into a .ipynb.
    """
    script_path = Path(script_path)
    ipynb_path = Path(ipynb_path)

    text = script_path.read_text(encoding="utf-8")
    lines = text.splitlines()

    cells = []
    current_kind = None  # "code" or "markdown"
    current_lines = []

    def flush_cell():
        nonlocal current_kind, current_lines
        if current_kind is None:
            return

        if current_kind == "markdown":
            md_lines = []
            for l in current_lines:
                if l.startswith("# "):
                    md_lines.append(l[2:])
                elif l.startswith("#"):
                    md_lines.append(l[1:].lstrip())
                else:
                    md_lines.append(l)
            source = "\n".join(md_lines).rstrip()
            cells.append(new_markdown_cell(source=source))

        elif current_kind == "code":
            source = "\n".join(current_lines).rstrip()
            cells.append(new_code_cell(source=source))

        current_kind = None
        current_lines = []

    for line in lines:
        if line.startswith("# %%"):
            flush_cell()
            if "[markdown]" in line:
                current_kind = "markdown"
            else:
                current_kind = "code"
            current_lines = []
        else:
            current_lines.append(line)

    flush_cell()

    nb = new_notebook(cells=cells, metadata={})
    nbformat.write(nb, ipynb_path)
    print(f"{script_path} -> {ipynb_path}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Convert between .ipynb and .py (percent-style) based on file extension."
    )
    parser.add_argument("input", help="Input .ipynb or .py file")
    parser.add_argument(
        "output",
        nargs="?",
        help="Optional output file. If omitted, uses same name with swapped extension.",
    )

    args = parser.parse_args()

    inp = Path(args.input)
    if not inp.exists():
        raise SystemExit(f"Input file does not exist: {inp}")

    if inp.suffix not in {".ipynb", ".py"}:
        raise SystemExit("Input must be a .ipynb or .py file")

    if args.output:
        out = Path(args.output)
    else:
        if inp.suffix == ".ipynb":
            out = inp.with_suffix(".py")
        else:
            out = inp.with_suffix(".ipynb")

    if inp.suffix == ".ipynb":
        ipynb_to_percent_script(inp, out)
    else:
        percent_script_to_ipynb(inp, out)
