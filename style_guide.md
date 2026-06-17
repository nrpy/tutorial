# NRPy2 Tutorial Notebook Style Guide

This guide captures formatting and pedagogy patterns worth preserving from an
audit of 65 notebooks in `nrpytutorial/`, cross-checked against current tutorial
and sample-code documentation guidance. It is intended for active NRPy2 tutorial
notebooks, not as a compatibility guide for old NRPy+ code.

## Core Principle

An NRPy2 tutorial notebook should be a guided learning experience. It should ask
the learner to do concrete work, show meaningful results early and often, and
connect symbolic physics, generated code, and numerical evidence.

Do not write notebooks as compact reference manuals. Do not make them depend on
unstated expert knowledge. A weakly prepared physics student should be able to
follow the sequence, know what to run, know what to look for, and understand why
the result matters.

## Standard Notebook Shape

Use this structure for most active tutorials:

```markdown
# Notebook Title

One short paragraph stating what this notebook builds, checks, or demonstrates.

Navigation: [Index](../index.ipynb) | Previous: [...] | Next: [...]

## Learning Goals

- Concrete action goal.
- Physics or numerical-methods goal.
- Generated-code or validation goal, if relevant.

## Words for This Notebook

- **Term:** plain-language definition.
- **Term:** plain-language definition.

## Challenges

Use this only when the notebook resolves non-obvious numerical, physical, or
software obstacles.

## Optional Short Setup or Notation

Use only when the first code cell needs symbols, conventions, or assumptions.

## Workspace Setup

Use this only for notebooks that generate files, build programs, or write
diagnostics.

## Step 1: Specific Action

Short explanation, then code.

## Step 2: Specific New Action

Short explanation, then code.

## Validation Check

Residual, comparison, plot, generated-code inspection, or runtime check.

## Learning Check

One short prompt asking the learner to predict, explain, compare, or identify.

## Continue

Next notebook link.
```

Short command-only setup notebooks may omit learning-goal scaffolding if a
README-style quick start is clearer. They must remain markdown-only unless there
is a strong reason to execute code.

## 14 Patterns to Preserve

### 1. Strong Opening Block

Start with a title, one useful purpose paragraph, and navigation. The old
notebooks usually opened with title, author, summary, and source links. Keep the
clarity of that pattern, but update it for NRPy2.

Good:

```markdown
# Finite Differences

Approximate derivatives from neighboring grid values, check the stencil on a
polynomial, and emit the corresponding generated C assignment.

Navigation: [Index](../index.ipynb) | Previous: [...] | Next: [...]
```

Avoid:

```markdown
# finite_difference.py

This notebook presents the API.
```

Reasons:

- The learner needs to know what they will accomplish.
- A title alone is not enough.
- Avoid "API" unless the notebook immediately defines it in plain language.

### 2. Table of Contents for Long Notebooks

Use a table of contents when a notebook is long enough that scrolling becomes a
burden. The old NRPy+ notebooks used this heavily and consistently.

Use for:

- Long start-to-finish project notebooks.
- Infrastructure notebooks with many generated files.
- ADM/BSSN or GRMHD derivations with many sections.

Skip for:

- Short notebooks with fewer than roughly 8 sections.
- Command-first setup pages.

Keep headings unique. Do not repeat generic headings such as "Generated Code",
"Output", or "Example" unless the surrounding title makes the section unique.

### 3. Numbered, Action-Oriented Section Headings

The old tutorials often used `Step 1`, `Step 2.a`, and similar headings. Keep
that structure when there is a real sequence.

Good:

```markdown
## Step 3: Check the Spherical Metric-Inverse Identity
```

Weak:

```markdown
## Step 3: Code
```

Rules:

- Use numbered steps only when order matters.
- The heading must say what is new.
- Substeps should be used for meaningful decomposition, not for every tiny cell.
- If a section adds no new idea, remove it.

### 4. Preliminaries or Notation Before Code

Many strong old notebooks include an introduction, notation note, or
preliminaries section before tensor-heavy code. Keep this pattern.

Use it for:

- Tensor index conventions.
- Coordinate names and basis choices.
- ADM/BSSN variables.
- Finite-difference stencil notation.
- Generated-project file roles.

Keep it short. A preliminaries section should prepare the first code cell, not
become a textbook chapter.

### 5. Challenge-First Framing

Several effective old notebooks begin difficult topics by naming the concrete
obstacles. This is especially useful in computational physics, where the code
often exists to handle a subtle failure mode.

Use this for:

- boundary-condition complications;
- coordinate singularities;
- floors, limiters, and physical bounds;
- shock handling;
- interpolation at faces or ghost zones;
- multiple coordinate or implementation variants.

Good:

```markdown
## Challenges

- **Inner boundaries:** ghost-zone points may map back into the physical grid.
- **Parity:** vector components may change sign across a mapped boundary.
- **Coordinate singularities:** spherical coordinates are singular at the axis.

The next sections address these one at a time.
```

Rules:

- State the obstacle before presenting the solution.
- Keep each challenge concrete.
- Map each challenge to a later section, code cell, or validation check.
- Do not use this section for generic motivation.

### 6. Math-to-Code Pairing

A high-value NRPy tutorial pattern is:

1. Show the equation.
2. Show the symbolic Python representation.
3. Check a residual or identity.
4. Generate code or run the numerical example.

Example shape:

```markdown
The one-dimensional second derivative is approximated by a stencil:

$$
\partial_x^2 u(x_i) \approx
\frac{-u_{i-2} + 16u_{i-1} - 30u_i + 16u_{i+1} - u_{i+2}}
{12 \Delta x^2}.
$$

The next cell asks NRPy for the same coefficients and compares them with this
formula.
```

Rules:

- Do not show equations without connecting them to code.
- Do not show code without saying which equation it represents.
- Use residuals when possible: zero residuals are understandable evidence.

### 7. Reproducible Workspace Setup

Project-generation notebooks should make their file-writing behavior explicit.
Many old start-to-finish and infrastructure notebooks created source directories
or output folders before generating code. Keep the reproducibility goal, but use
clean NRPy2-era paths and avoid old global path hacks.

Use this when a notebook:

- writes generated C files;
- creates a project directory;
- builds or runs an executable;
- writes diagnostic outputs;
- compares generated files against trusted files.

Good:

```python
from pathlib import Path
import tempfile

workspace_manager = tempfile.TemporaryDirectory(
    prefix="nrpy_tutorial_wave_", dir=Path.cwd()
)
WORKSPACE = Path(workspace_manager.name)
PROJECT_DIR = WORKSPACE / "project" / "wave_equation_cartesian"
print("workspace:", WORKSPACE)
```

Rules:

- Print the workspace or project path.
- Keep generated files in a predictable workspace.
- Clean or recreate generated directories intentionally.
- Do not depend on hidden current-directory state.
- Do not use `sys.path` hacks in active NRPy2 notebooks.
- Do not put execution-environment repair code in learner-facing notebooks
  unless the environment is the concept being taught. Cache directories,
  writable-home settings, and CI/kernel-launch settings belong in the test
  harness, setup documentation, or NRPy internals.

### 8. Small Executable Cells with Visible Output

The best old notebooks interleave explanation, code, and evidence. Keep that.

Rules:

- Prefer several small runnable cells over one giant cell.
- Every nontrivial code cell should produce evidence: printed values, generated
  code, a plot, a file listing, a residual, or a runtime check.
- Setup/import cells may be output-free, but they should be clearly labeled.
- Break long Python function calls over multiple lines.

Good:

```python
generated = ccg.c_codegen(
    [x + y, x * y, x**2 - y**2],
    ["sum_xy", "prod_xy", "diff_sq"],
    include_braces=False,
    enable_cse=False,
    verbose=False,
)
print(generated)
```

Avoid:

```python
print(ccg.c_codegen([x + y, x * y, x**2 - y**2], ["sum_xy", "prod_xy", "diff_sq"], include_braces=False, enable_cse=False, verbose=False))
```

### 9. Explicit Validation Sections

Validation was one of the strongest recurring old-notebook patterns. Preserve it
as a named section, not a hidden afterthought.

Use validation for:

- Symbolic identities, such as metric-inverse products.
- Round-trip conversions, such as ADM to BSSN and back.
- Stencil residuals on test polynomials.
- Generated-code comparisons.
- Convergence checks.
- Runtime diagnostic comparisons.

Preferred section names:

```markdown
## Validation Check
## Check the Residual
## Compare Against the Hand Formula
## Verify the Generated Project Output
```

Validation cells should fail loudly when the expected result is not obtained.
Use `raise RuntimeError(...)` or an equivalent direct check.

Prefer semantic validation over formatter-sensitive string matching. Use
residuals, object metadata, parsed values, or minimal concept-bearing generated
identifiers before checking exact generated-source text.

### 10. Validation as a Unit-Test Workflow

Some old notebooks go beyond a final residual check: they teach how a test case
is built. Keep this pattern for algorithms where correctness is subtle.

Use this when:

- the notebook compares against trusted output;
- arbitrary analytic fields are used as test data;
- generated code is tested against another implementation;
- a tolerance or error norm matters;
- the notebook is about a reusable algorithm rather than a single formula.

Recommended shape:

```markdown
## Build a Test Case

Define analytic fields simple enough to evaluate, but rich enough to exercise
all terms in the algorithm.

## Run the New Calculation

Generate or evaluate the NRPy2 result.

## Compare Against Trusted Output

Print the error, tolerance, and pass/fail result.
```

Rules:

- State what is trusted and why.
- State what is newly computed.
- Explain the tolerance in plain language.
- Use analytic data when real data would hide the logic.
- Make failure explicit.
- Tie runtime checks to the concept being taught, not incidental whitespace or
  pretty-printing in generated source.

### 11. Full Generated Artifacts When They Teach the Concept

The old ETK, WaveToy, and infrastructure notebooks often exposed generated C,
headers, CCL files, and build metadata. Keep this when the learner is meant to
understand the generated artifact.

Rules:

- Full source dumps are acceptable when they illustrate a concept.
- Before the dump, tell the learner what to look for.
- Do not replace meaningful generated source with a vague summary.
- Do not use "excerpt" or "snippet" when the omitted part matters.

Good framing:

```markdown
The full `rhs_eval.c` file is printed below. On a first pass, look for:

- the function name;
- the grid loop;
- grid reads used by the finite-difference stencil;
- assignments to right-hand-side fields.
```

Generated output should be treated as evidence, not decoration.

### 12. Catalog Tables for Named Methods, Parameters, and Variants

Many old notebooks use named dictionaries, tables, or catalogs: Butcher tables,
Hamiltonian terms, runtime parameters, primitive-variable sets, coordinate
choices, and generated files. Keep this when learners need to compare options.

Use tables for:

- method choices;
- coordinate variants;
- runtime parameters;
- generated files and their roles;
- named data structures;
- test-case inputs and expected outputs.

Good:

```markdown
| Name | Purpose | Where It Appears | What to Inspect |
| --- | --- | --- | --- |
| `wave_speed` | Sets propagation speed | parameter file | value used by RHS |
| `rhs_eval.c` | Updates time derivatives | generated source | grid loop and RHS assignments |
```

Rules:

- Each row should answer a learner's comparison question.
- Keep columns few and concrete.
- For code dictionaries, print or summarize keys before implementation details.
- Do not use tables merely to make prose look organized.

### 13. Exercises and Learning Checks

Old NRPy+ notebooks used exercises less often than they used derivations and
validation, but the exercise pattern is worth expanding in NRPy2.

Use short prompts:

- Predict what the next cell should print.
- Change one parameter and rerun.
- Identify which term came from geometry.
- Compare the coarse and fine errors.
- Explain why a residual should be zero.

Good:

```markdown
## Learning Check

Before running the residual cell, predict which terms should cancel. After
running it, explain why a zero residual is stronger evidence than visual
similarity.
```

Avoid long homework-style problem sets inside a first-pass tutorial. Link to
extensions or solution notebooks when needed.

Place prediction prompts before the cell they refer to. If the prompt appears
after the computation, phrase it as reflection or explanation instead of
"before running".

### 14. References and Scientific Provenance

Physics-heavy tutorials should cite the model, equation, or paper where it first
matters. Several old notebooks did this well with links to arXiv, journal
articles, or background references.

Rules:

- Put citations near the relevant equation or model.
- Keep citation text short.
- Do not bury all references at the end.
- Use references to support physics, not to compensate for missing explanation.

Example:

```markdown
The Brill-Lindquist conformal factor below follows the original
[Brill and Lindquist initial-data construction](https://doi.org/10.1103/PhysRev.131.471).
```

## Patterns to Avoid

Do not carry these old-notebook habits into NRPy2:

- Google Analytics scripts in notebooks.
- Old `../edit/...` links.
- Universal LaTeX/PDF export cells.
- Historical NRPy+ imports or old flat module names in active NRPy2 examples.
- Repeated generic headings.
- Long one-line Python examples.
- Large helper cells without an explanation of whether students should read
  them closely.
- Source dumps without "what to look for" guidance.
- Cache, path, or environment monkeypatches inside concept notebooks.
- Formatter-sensitive validation that fails because generated whitespace or
  pretty-printing changed.
- Broken or speculative links.
- Comments warning that removed notebooks may break links. Fix the links instead.

## Language Rules

Use plain, direct language.

Prefer:

- "function call"
- "module"
- "generated C code"
- "code-writing path"
- "runtime setting"
- "grid field"
- "right-hand side"

Avoid or define immediately:

- "API"
- "backend"
- "registry"
- "prototype"
- "thorn"
- "CCL"
- "lapse"
- "shift"
- "extrinsic curvature"
- "conformal factor"

When a specialized term is necessary, define it in `## Words for This Notebook`
or in the sentence where it first appears.

## Code Style Rules

- Use current NRPy2 imports only.
- Keep source-cell lines at or below 100 characters when practical.
- Use multi-line calls for generated-code examples.
- Use descriptive temporary variables before printing complex generated output.
- Use assertions or explicit runtime checks for validation, but keep those
  checks tied to the concept being taught.
- Set up workspaces explicitly in notebooks that write files.
- Use full generated-file reads when the file itself is the lesson.
- Keep helper functions in clearly marked cells.
- Tell beginners whether a helper cell should be skimmed or studied.

## Output Rules

Every important notebook should include at least one of:

- printed symbolic expressions;
- residual checks;
- generated C output;
- generated file contents;
- diagnostic tables;
- plots;
- file inventories.
- catalog tables for methods, parameters, variants, or generated files.

For numerical-methods notebooks, prefer visual evidence when it improves
understanding:

- stencil-weight plots;
- wave-profile plots;
- convergence-history plots;
- coordinate-map plots;
- diagnostic-error plots.

Plots should have labels, legends when needed, and titles that state the
comparison being made.

## Review Checklist

Before merging a tutorial notebook, check:

- The notebook has a clear title and purpose.
- Navigation links resolve.
- The section headings are unique and action-oriented.
- Specialized terms are defined locally.
- Long Python lines are broken into readable blocks.
- Complex algorithms name their concrete challenges before solving them.
- File-generating notebooks set up and print an explicit workspace.
- Every meaningful code cell has visible evidence or a clear setup role.
- The notebook includes a named validation section when it computes anything
  symbolic or numerical.
- Validation checks target mathematics, metadata, generated identifiers, or
  runtime behavior, not fragile whitespace in generated source.
- Subtle algorithms show how their test case is built, not only the final
  pass/fail result.
- Tables are used when learners must compare methods, parameters, variants, or
  generated files.
- Generated source is complete when the source is concept-bearing.
- Full source dumps include "what to look for" guidance.
- The notebook executes cleanly from top to bottom.
- Stored notebook outputs contain no warnings, errors, or tracebacks. External
  kernel-launch warnings from execution tools should be handled by the test
  command or harness, not by adding environment hacks to the lesson.
- There are no stale old NRPy+ names, deleted-notebook links, or historical
  setup hacks.

## References

- Diataxis, "Tutorials": https://diataxis.fr/tutorials/
  - Used for the principle that tutorials are learning-oriented, practical,
    concrete, and should deliver visible results early and often.
- Google for Developers, "Creating sample code":
  https://developers.google.com/tech-writing/two/sample-code
  - Used for the principles that sample code should be correct, concise,
    understandable, reusable, tested, and accompanied by setup and expected
    output.
- Google Codelabs: https://codelabs.developers.google.com/
  - Used as a model for guided, hands-on coding tutorials that move learners
    through a concrete sequence.
- The Carpentries, "Collaborative Lesson Development":
  https://carpentries.org/lesson-development/
  - Used for lesson-design framing and collaborative open-source lesson
    maintenance.
- The Carpentries lesson collection: https://carpentries.org/lessons/
  - Used as a reference point for structured computational lessons aimed at
    learners building practical skills.

## Audit Basis

This guide is based on inspection of 65 notebooks from `nrpytutorial/`,
excluding `.ipynb_checkpoints/`, `Deprecated/`, and `old/` paths. The inspected
set included core NRPy+ concept notebooks, finite-difference notebooks,
reference-metric notebooks, scalar-wave start-to-finish notebooks, ETK thorn
notebooks, BHaH notebooks, and IllinoisGRMHD documentation notebooks.

It was then extended after a second audit of 36 additional randomly selected
non-deprecated notebooks from the remaining `nrpytutorial/` pool, using random
seed `20260617`. That second pass emphasized challenge-first framing,
reproducible workspace setup, validation as a unit-test workflow, and catalog
tables for named methods, parameters, and variants.
