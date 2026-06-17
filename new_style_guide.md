# NRPy Tutorial Notebook Style Guide

## Ground Truth, Audience, and Authority

This guide captures the tutorial style embodied by the curated notebooks in
`orig_tutorial/`. That directory is the frozen canonical tutorial corpus for
this guide and is to be treated as equivalent to the notebooks at commit
`33ed50470f9c08a21d5daa5ad0dda5b419302fd5` of this repository.

The guide is prescriptive for active NRPy tutorial notebooks. The old notebooks
provide the style evidence; this guide decides how that evidence is applied
today.

Assume a weakly prepared physics or numerical-relativity learner who has basic
Python exposure and can read elementary equations, but who does not know NRPy's
infrastructure, BHaH conventions, Einstein Toolkit files, or the local codebase.

The learner should never need to infer why a term, variable, code object, or
generated file matters. The notebook must say where each new concept fits in
the physical, numerical, or code-generation workflow before the concept is used
in code.

Review authority order:

1. Explicit current requirements in this guide.
2. User-specified constraints for the current notebook or notebook family.
3. Recurring patterns in the frozen `orig_tutorial/` corpus.
4. Legacy behavior in old notebooks, only when it does not conflict with the
   first three items.

Historical artifacts that are not current style include:

- old source links such as `../edit/...`;
- silent concept-bearing cells;
- absolute user-local paths;
- object-only display reprs;
- PDF/export cells unrelated to the lesson;
- deliberately abbreviated outputs.

Exceptions must be visible to reviewers. Put the exception, rationale, and
scope in the notebook itself or in a notebook-family README or review policy.

## Core Principle

An NRPy tutorial is a guided computational physics lesson. It should not read
like a compact API reference, a command transcript, or a list of disconnected
terms.

Every notebook should make the learner understand:

- what physical, mathematical, or infrastructure problem is being solved;
- why the next code cell is needed;
- how equations map to NRPy data structures;
- how NRPy maps symbolic expressions to generated code;
- what output proves that the calculation, code generation, or runtime behavior
  is correct.

Ground first, name second. Do not introduce a symbol, function, field, C object,
infrastructure option, or generated artifact before explaining what it
represents and where it fits in the larger algorithm.

## Author and Reviewer Workflow

Use this guide in this order:

1. Choose one primary archetype from the archetype selection matrix.
2. Start from that archetype's contract and template.
3. Apply universal rules for openings, headings, grounding, code, outputs, and
   validation.
4. Apply specialized overlays for CFunction, BHaH, finite differences, generated
   projects, plots, or scientific references.
5. Execute the notebook from a fresh kernel.
6. Inspect stored outputs, generated artifacts, links, and `git status`.
7. Complete the pass/fail review checklist.

Every executable tutorial should be written so a learner can run it from a
clean kernel with the notebook toolbar. The standard opening instruction is:

```markdown
To run the whole notebook, click the `>>` toolbar button and choose
**Restart Kernel and Run All Cells...**.
```

Do not add a separate "Setup" step unless the notebook itself creates a
workspace, writes files, builds an executable, or teaches environment setup.

## Archetype Selection Matrix

Choose one primary archetype before writing. Specialized patterns are overlays,
not separate primary archetypes.

- **Explanatory/Core Module Tutorial:** use when the notebook teaches one NRPy
  module or concept family. Required evidence is small visible output after each
  concept, such as formulas, registry keys, generated source, or object
  metadata. Required validation is a recap, identity check, comparison, or
  metadata/source inspection.
- **Ten-Minute Overview:** use for compact first contact with NRPy. Required
  evidence is one running example, visible indexed expressions, complete
  generated C for a small example, and a grounded CFunction or code-generation
  inspection. Required validation is at least one symbolic, generated-code, or
  registry check proving the workflow.
- **Physics or Numerical-Methods Tutorial:** use for equations,
  discretizations, convergence tests, or physical diagnostics. Required evidence
  is equations, variable meanings, algorithm output, clarifying plots, and
  diagnostic tables. Required validation is an exact-solution, residual,
  trusted-module, tolerance, or convergence check.
- **Start-to-Finish Project or Infrastructure Tutorial:** use when the notebook
  writes files, builds projects, runs executables, or generates infrastructure.
  Required evidence is a workspace path, generated-file catalog, complete
  inventories, build/run logs, and selected complete generated artifacts.
  Required validation is generated-file checks, build/run checks, runtime
  diagnostics, or convergence behavior.
- **Index Notebook:** use for tutorial navigation only. Required evidence is
  clear grouped links. There is no execution-output requirement.

Overlap rule:

- A notebook has exactly one primary archetype.
- CFunction, BHaH, finite-difference, plotting, and project rules are overlays.
- If compactness conflicts with grounding, complete evidence, or validation,
  grounding, complete evidence, and validation win.
- Ten-minute tutorials must use the smallest complete example that proves the
  point. They must not use excerpts or unexplained terms to stay short.

## Archetype Contract: Explanatory/Core Module Tutorial

Use this for notebooks that teach NRPy concepts such as indexed expressions,
parameters, grid functions, reference metrics, finite differences, C code
generation, or C-function registration.

Required sequence:

1. Title, author, run-all instruction, purpose paragraph.
2. Required reading, if the notebook assumes knowledge beyond basic Python,
   basic SymPy, undergraduate mathematics, or the immediately previous tutorial.
3. Source-code links, if teaching a specific NRPy module.
4. Table of contents when required by the heading rules.
5. `# Words for This Notebook` or `# Notation and Terms`, if specialized terms
   appear.
6. Numbered steps that introduce one concept at a time.
7. Visible evidence after every nontrivial concept.
8. Named validation, recap, or comparison section.
9. Short exercises or "What next?" section when useful for continuity.

Pass criteria:

- Every term introduced in a code cell was grounded earlier or in the sentence
  immediately before the cell.
- Every nontrivial cell either prints evidence or is immediately verified by
  the next cell.
- The final section tells the learner what was proven, stored, generated, or
  compared.

### Template: Explanatory/Core Module Tutorial

Use this template as a complete structural model. Replace bracketed labels with
real notebook-specific content.

```markdown
# [Concept or Module Name]

## Author: [author name]

To run the whole notebook, click the `>>` toolbar button and choose
**Restart Kernel and Run All Cells...**.

This notebook shows [what the learner constructs], [what NRPy object or module
is being taught], and [what output will verify the result].

### Required Reading

- [required-reading-title]

### NRPy Source Code

- [source-code-link]: [role of the source file]

# Table of Contents

1. [Words for This Notebook](#Words-for-This-Notebook)
1. [Step 1](#Step-1:-Initialize-the-concept): Initialize the concept.
1. [Step 2](#Step-2:-Build-the-first-example): Build the first example.
1. [Step 3](#Step-3:-Inspect-the-result): Inspect the result.
1. [Validation Check](#Validation-Check): Verify the expected behavior.
1. [What next?](#What-next?)

# Words for This Notebook

- **[term]:** [plain-language definition and role in the workflow].

# Step 1: Initialize the concept
### [Back to [top](#Table-of-Contents)]

[Explain what this cell imports or initializes, why that setup is needed, and
what the output should show.]

# Step 2: Build the first example
### [Back to [top](#Table-of-Contents)]

[State the mathematical, physical, or infrastructure object first. Then name
the NRPy or Python object that will represent it.]

# Step 3: Inspect the result
### [Back to [top](#Table-of-Contents)]

[State the inspection question before printing output.]

# Validation Check
### [Back to [top](#Table-of-Contents)]

[State what is trusted, what is newly computed, and what pass/fail condition is
used.]

# What next?

[Link to the next notebook or topic.]
```

## Archetype Contract: Start-to-Finish Project or Infrastructure Tutorial

Use this for notebooks that write files, build projects, register multiple
generated artifacts, run executables, create thorns, emit CCL files, or produce
runtime diagnostics.

Required sequence:

1. Title, author, run-all instruction, purpose paragraph.
2. `Notebook Status` and `Validation Notes`.
3. Table of contents.
4. `# Words for This Notebook`, including infrastructure terms before use.
5. `# Workspace and Generated Files`, before any file-writing cell.
6. Generated-file catalog, including role and inspection target for each key
   artifact.
7. Generation or registration sections.
8. Project construction section.
9. Build/run section, with terminal-ready commands if the learner must leave
   Jupyter.
10. Named validation section.
11. Cleanup or "What next?" section if needed.

Pass criteria:

- The notebook prints the workspace or project path before writing files.
- The notebook states whether generated directories are created, cleaned,
  reused, or updated in place.
- All key generated files are listed.
- Complete file inventories are printed when file generation is the lesson.
- The validation proves that the generated project, build, runtime behavior, or
  diagnostics are correct enough for the tutorial claim.

### Template: Start-to-Finish Project or Infrastructure Tutorial

```markdown
# [Start-to-Finish Task Name]

## Author: [author name]

To run the whole notebook, click the `>>` toolbar button and choose
**Restart Kernel and Run All Cells...**.

This notebook generates [project or infrastructure artifact], builds or runs
[executable or workflow], and validates [diagnostic or convergence claim].

**Notebook Status:** [Validated / Draft / Requires external run]

**Validation Notes:** [State the final validation claim and where it appears.]

# Table of Contents

1. [Words for This Notebook](#Words-for-This-Notebook)
1. [Workspace and Generated Files](#Workspace-and-Generated-Files)
1. [Step 1](#Step-1:-Generate-or-register-core-artifacts): Generate artifacts.
1. [Step 2](#Step-2:-Write-the-project): Write the project.
1. [Step 3](#Step-3:-Build-and-run): Build and run.
1. [Validation Check](#Validation-Check): Validate behavior.
1. [What next?](#What-next?)

# Words for This Notebook

- **Project directory:** The directory containing generated source, metadata,
  build files, runtime inputs, and diagnostics.
- **Generated artifact:** A file or registered C function produced by NRPy and
  inspected or used later in the notebook.

# Workspace and Generated Files
### [Back to [top](#Table-of-Contents)]

This notebook writes [project directory]. Each run [cleans/reuses/updates] that
directory. The generated artifacts are:

| Artifact | Role | Where used | Inspect |
| --- | --- | --- | --- |
| `[artifact-name]` | [workflow role] | [section] | [field or loop] |

# Step 1: Generate or register core artifacts
### [Back to [top](#Table-of-Contents)]

[Ground the generated functions, files, or metadata before the code.]

# Step 2: Write the project
### [Back to [top](#Table-of-Contents)]

[State which files are written and print a complete generated-file inventory.]

# Step 3: Build and run
### [Back to [top](#Table-of-Contents)]

Run these commands from a terminal, if the notebook does not run them directly:

```bash
cd [project-directory]
[build-command]
[run-command]
```

# Validation Check
### [Back to [top](#Table-of-Contents)]

[Print the error, diagnostic, convergence table, generated-file check, or
runtime pass/fail output.]

# What next?

[Link to the next detailed notebook or project variant.]
```

## Archetype Contract: Ten-Minute Overview

Use this for compact first-contact notebooks.

Required sequence:

1. Title, author, run-all instruction, purpose paragraph.
2. Table of contents.
3. One running example from physics or numerical relativity.
4. Motivation for why NRPy helps with that example.
5. Einstein-like indexed notation before NRPy tensor code when tensor machinery
   is being introduced.
6. Complete generated C output for a small enough example.
7. A grounded CFunction registration or generated-function inspection.
8. Finite-difference-aware code only after derivative naming, gridfunctions,
   stencil order, and memory access have been defined.
9. "What next?" links.

Pass criteria:

- The notebook does not define random terms disconnected from the running
  example.
- Each new term is introduced only when the example needs it.
- Compactness never removes physical meaning, algorithmic context, complete
  generated evidence, or validation.

Preferred running example:

- Spatial Christoffel symbols from a metric and its first derivatives.
- The example should state the equation in indexed notation, define index
  ranges and symmetry, map tensors to NRPy data structures, generate C, and
  inspect or register one complete generated function.

## Archetype Contract: Physics or Numerical-Methods Tutorial

Use this for wave equations, finite differences, convergence tests, initial
data, or similar physics-facing material.

Required sequence:

1. Title, author, run-all instruction, purpose paragraph.
2. `Notebook Status` and `Validation Notes`.
3. Prerequisites or required reading when the method assumes background.
4. Complete initial-value-problem statement before implementation.
5. Algorithm description before loops and arrays.
6. Implementation steps with visible evidence.
7. Visual evidence when it clarifies a comparison or trend.
8. Named validation section.

The initial-value-problem statement must include:

- governing equation;
- domain;
- coordinates or basis;
- evolved variables;
- auxiliary variables;
- units or normalization;
- initial data;
- boundary conditions;
- diagnostics and their physical meaning;
- expected analytic or numerical behavior.

Wave-equation notebooks must define:

- `u`: the wave amplitude or model-specific field;
- `v`: the auxiliary time derivative or other model-specific auxiliary field;
- wave speed;
- initial data;
- boundary conditions;
- Method of Lines, if used;
- energy density, including whether the density is per unit length, area,
  volume, coordinate volume, mass, or another model-specific normalization.

Pass criteria:

- Equations appear near the code that implements them.
- Main variables have physical meanings before code use.
- The validation uses an exact solution, residual, trusted module, tolerance, or
  convergence expectation.
- Numerical comparisons print the norm type, resolutions, errors, expected
  order, measured order, tolerance rationale, and pass/fail result.

## Archetype Contract: Index Notebook

Use this for navigation-only tutorial indexes.

Required sequence:

1. Title.
2. One short statement of what the index organizes.
3. Grouped learning paths.
4. Link text that identifies the task or topic, not only the filename.
5. Deprecated or historical material clearly labeled, if present.

Rules:

- Do not include code cells unless the index intentionally generates its own
  contents.
- There is no execution-output requirement.
- Links must resolve to existing notebooks, source files, or documentation.

## Reviewable Terms

Use these definitions when reviewing. They are intended to remove subjective
interpretation.

- **Active executable tutorial:** A notebook meant to be opened and run by
  learners. Index-only notebooks are not executable tutorials.
- **Setup cell:** A code cell containing only imports, global parameter choices,
  registry clearing, path-free constants, or environment-independent
  initialization.
- **Helper cell:** A cell that defines functions or classes used later and does
  not perform the main lesson calculation.
- **Project-generation cell:** A cell that writes files or registers generated
  artifacts whose effects are verified in the next relevant cell.
- **Nontrivial code cell:** Any code cell that is not a setup cell, helper cell,
  or project-generation cell immediately verified by later evidence.
- **Long code cell:** A source cell with more than 50 lines.
- **Main variable:** Any variable in the governing equation, evolved state,
  auxiliary state, initial data, boundary condition, diagnostic, plot,
  validation, generated-code interface, or learner-facing catalog.
- **Required evidence output:** Output that proves or illustrates formula
  correctness, generated source shape, registry state, generated file content,
  runtime result, convergence claim, plotted comparison, or file-writing effect.
- **Dense output:** Generated source, CCL files, registry dumps, matrices,
  arrays, tables, logs, file inventories, plots, or nested data structures with
  enough detail that the learner needs guidance on what to inspect.
- **Complete meaningful artifact:** One bounded unit the learner is asked to
  inspect, such as one full generated C function, one full generated file, one
  complete generated-file inventory, one complete validation log, one full
  registered-object table, or one complete labeled plot.
- **Key generated file:** Any generated file referenced in prose, needed by
  build/run commands, used in validation, or necessary to explain the generated
  project.
- **Trusted result:** The analytic expression, exact solution, tested module,
  existing implementation, known metadata, or convergence expectation against
  which new notebook output is compared.

Replace vague language with these terms. For example, do not say "show important
files"; say "print every key generated file or a complete inventory plus the
complete representative file named in the inspection checklist."

## Universal Opening and Navigation Rules

Required in every executable tutorial:

- a title naming the subject, not only a module filename;
- `## Author:` or `## Authors:` with accurate credit;
- the standard run-all instruction;
- a purpose paragraph that says what the notebook constructs, checks,
  validates, or generates.

Additional requirements:

- Add `Notebook Status` and `Validation Notes` for physics,
  numerical-methods, and start-to-finish notebooks.
  Treat this as a first-page validation contract: the notebook must later prove
  the stated claim in a named validation section.
- Add required reading links when the notebook assumes knowledge beyond basic
  Python, basic SymPy, undergraduate mathematics, or the immediately previous
  tutorial.
- Core module tutorials must include required reading unless the opening states
  that the notebook is fully self-contained.
- Add source-code links when the notebook teaches a specific NRPy module or
  generated infrastructure.
- Source links must identify the module or generated infrastructure role, not
  merely point at a filename.
- Add index, previous, and next links when the notebook belongs to an ordered
  sequence.

## Headings and Table of Contents

The frozen `orig_tutorial/` notebooks intentionally use `# Step N` headings at
the same markdown level as the title. Preserve that style for compatibility
with the established notebook outline and anchor links, even though it differs
from a conventional document outline.

Use this heading hierarchy in tutorial notebooks:

- notebook title: `# Notebook Title`;
- table of contents: `# Table of Contents`;
- major steps: `# Step N: Specific Action`;
- meaningful substeps: `## Step N.a: Specific Subaction`;
- back-to-top links: `### [Back to [top](#Table-of-Contents)]`.

Rules:

- A table of contents is required when the notebook has at least three major
  sections, any substeps, or more than eight total cells.
- If a table of contents exists, add a back-to-top link under every major step
  and substep.
- Use numbered steps only when order matters.
- Use substeps only for meaningful decomposition, not for every small cell.
- Heading text must identify the new action or concept.
- Heading anchors must be unique and stable.
- Do not repeat generic headings such as "Code", "Output", or "Example" unless
  the surrounding title makes the action unique.

## Words, Notation, and Grounding

Add `# Words for This Notebook` or `# Notation and Terms` before the first code
cell when a notebook introduces any of the following:

- more than five specialized terms;
- tensor index conventions;
- PDE variables or auxiliary variables;
- BHaH, Einstein Toolkit, CCL, thorn, or generated-project terminology;
- finite-difference stencil notation;
- C-function registration terminology.

Always define these common domain terms when they appear:

- wave equation notebooks: `u`, `v`, wave speed, initial data, boundary
  conditions, Method of Lines, energy density if used;
- finite-difference notebooks: stencil, finite-difference order, centered,
  upwind, downwind, ghost zone if used;
- tensor notebooks: index position, symmetry, contraction, implied sum,
  dimension, basis or coordinate system;
- CFunction notebooks: C function, prototype, parameter list, body, include,
  registration;
- BHaH or ETK notebooks: BHaH, gridfunction, CodeParameter, thorn, CCL,
  schedule, interface, parameter file, generated project.

Before defining code objects, state:

- the physical or mathematical object represented;
- the algorithmic role it plays;
- the data structure that will hold it;
- what output will verify or illustrate it.

Bad:

```markdown
Now define `v` and compute the energy density.
```

Good:

```markdown
The wave amplitude is `u(t,x)`. We introduce `v(t,x) = partial_t u(t,x)` so the
second-order wave equation can be written as two first-order-in-time equations.
The energy density used below is energy per unit coordinate length for this 1D
model normalization.
```

## Preliminaries and Challenge Framing

Use a short preliminaries or notation block before the first code cell whenever
the notebook begins with tensors, PDEs, finite differences, C-function
registration, generated projects, or infrastructure-specific artifacts.

The block should prepare the first few code cells, not become a textbook
chapter. Include only the needed items:

- symbols and index conventions;
- coordinate system and basis;
- units or normalization for physical variables;
- finite-difference stencil notation;
- generated artifact names and roles;
- what the first output will prove or illustrate.

Use challenge-first framing when the notebook exists to overcome a non-obvious
numerical, physical, symbolic, or software obstacle. State the obstacle before
presenting the solution, then map it to later steps, code cells, outputs, or
validation checks.

Good challenge framing:

```markdown
Challenge: the finite-difference derivative name `u_dDD01` must encode both the
base gridfunction and the derivative operator. Step 2 decodes the name, Step 3
builds the stencil, and the validation cell checks the generated memory reads.
```

Do not use challenge framing for generic motivation. Each challenge must connect
to a concrete later action.

## Math-to-Code Pattern

Use this pattern whenever a notebook translates equations into NRPy:

1. State the equation in mathematical notation.
2. Define the symbols, indices, coordinate system, and basis.
3. Map the equation to NRPy/Python data structures.
4. Implement the loops or helper calls.
5. Print, plot, or validate a complete result.

For tensor examples, start with Einstein-like notation when the purpose is to
teach NRPy's indexed machinery.

Rules:

- Do not show equations without saying which code objects represent them.
- Do not show code without saying which equation or algorithm it implements.
- When symmetry reduces independent components, state the full count, reduced
  count, and ordering used in any flat arrays.
- Prefer residuals and identities over visual similarity when validating
  symbolic mathematics.

## Code Cell Style

Rules:

- Put a short explanatory markdown cell before every nontrivial or long code
  cell.
- For long code cells, explicitly say whether the learner should skim or study
  the cell and name the artifact or effect it produces.
- Keep code cells focused on one conceptual task.
- A cell may combine tasks only when one generated artifact requires shared
  context or splitting the cell would hide the data flow being taught.
- Use comments to label meaningful steps inside longer cells.
- Use current NRPy imports and canonical aliases unless the lesson explicitly
  demonstrates an import variant.
- Keep source-cell lines at or below 100 characters unless a generated literal
  or external command makes this impractical.
- Avoid execution-environment repair code in learner-facing notebooks.

Canonical aliases:

- `import sympy as sp`
- `import nrpy.indexedexp as ixp`
- `import nrpy.c_codegen as ccg`
- `import nrpy.c_function as cfc`
- `import nrpy.grid as gri`
- `import nrpy.params as par`
- `import nrpy.reference_metric as refmetric`

Acceptable output-free cells:

- clearly labeled setup cells;
- helper cells whose purpose is explained immediately before the cell;
- BHaH-style registration helper definitions, if called and inspected in the
  next relevant cell;
- project-generation cells, if followed immediately by file inventories,
  printed paths, checks, or complete generated artifacts.

## Output Policy

Outputs are part of the lesson. They are not decoration.

Every nontrivial code cell must produce required evidence output unless it is
immediately verified by the next relevant cell.

### No-Truncation Rule

Truncation is forbidden for required evidence output.

Truncation includes:

- literal `...` used to replace omitted output;
- "selected lines shown" excerpts;
- first-N-lines or last-N-lines dumps when omitted lines matter;
- abbreviated generated source;
- shortened arrays, lists, matrices, tables, or SymPy expressions;
- pandas, NumPy, SymPy, or Jupyter abbreviated reprs;
- frontend-collapsed stored output;
- object-only reprs such as `<Figure ...>`, `<Image object>`, or
  `<IPython.lib.display.IFrame ...>`;
- terminal logs that hide failed commands or omitted file writes.

Do not use "first N lines" plus ellipsis. If the artifact is too large for a
single useful output, choose one of these alternatives:

- a smaller complete generated example;
- a complete generated-file inventory plus one complete representative file;
- separate complete artifacts across multiple cells;
- a complete machine-readable file written by the notebook and a printed path,
  when the file itself is the inspected artifact.

Excerpts are allowed only when the omitted content is unrelated to the lesson
and the markdown explicitly states that the excerpt is not required evidence.

### No-Truncation Review Procedure

Reviewers must check both the rendered notebook and the `.ipynb` JSON.

Pass requirements:

- Stored outputs come from one fresh restart-and-run-all execution.
- Required evidence outputs are not collapsed in the rendered notebook.
- Required evidence outputs do not contain ellipsis placeholders, selected-line
  helpers, object-only reprs, or abbreviated array/table/string reprs.
- Generated source shown as evidence is complete for the function, file, or
  bounded artifact named in the inspection checklist.
- Logs shown as evidence include failed commands, warnings, and relevant file
  writes.

A reviewer must flag truncation as a blocker when omitted content is needed to
understand or verify a formula, generated artifact, registry state, file write,
runtime result, plot, or convergence claim.

## Generated Code and Large Artifacts

Generated source is often the main evidence in NRPy tutorials. Treat it as a
first-class teaching artifact.

Rules:

- Show complete generated source when the structure of that source is the
  lesson.
- Do not dump unrelated project files inline.
- For project notebooks, print a complete inventory, then display the complete
  files the lesson asks learners to inspect.
- Introduce each artifact before printing it: function name, file role,
  infrastructure target, and what should appear inside.
- Generated source or generated files must answer an inspection question.
- Before dense output, provide an inspection checklist naming the fields, loops,
  assignments, files, or numerical quantities the learner should inspect.
- After displaying a generated artifact, include validation, comparison, or
  learner-facing interpretation stating what the artifact demonstrates.
- When generated code is compared against trusted output, state what is trusted
  and why.
- Avoid formatter-sensitive validation unless formatting is the concept. Prefer
  metadata, identifiers, residuals, file existence, parsed values, or complete
  generated files.

Good framing:

```markdown
The full `rhs_eval.c` file is printed below. Inspect:

- the function name;
- the loop over grid points;
- the gridfunction reads used by the stencil;
- the assignment to the right-hand-side array.
```

## Catalogs for Named Objects and Variants

Use a compact catalog whenever learners must compare named options, objects, or
artifacts.

Catalogs may be markdown tables, printed lists, or generated inventories. Table
syntax is not mandatory; completeness and comparison value are mandatory.

Use catalogs for:

- runtime or CodeParameters;
- coordinate systems and reference metrics;
- finite-difference methods, stencil orders, and upwind/downwind variants;
- gridfunctions and parity types;
- registered C functions;
- generated files and their roles;
- test cases, input data, and expected outputs;
- infrastructure variants such as BHaH, ETLegacy, or CarpetX.

Each catalog entry must answer:

- name;
- purpose;
- where it appears or how it is used;
- what the learner should inspect.

Example:

```markdown
| Name | Purpose | Where it appears | What to inspect |
| --- | --- | --- | --- |
| `fd_order` | Finite-difference order | parameter file | value used by RHS |
| `rhs_eval.c` | Updates RHS fields | generated source | grid loop and reads |
```

## Validation

Validation is required whenever a notebook computes symbolic expressions,
generates code, writes project files, or runs a numerical method.

Use explicit validation sections such as:

```markdown
# Validation Check
# Code Validation
# Error Analysis and Code Validation
# Compare Against the NRPy Module
# Convergence Test
```

Rules:

- Make failures loud with assertions, `RuntimeError`, nonzero exits, or explicit
  pass/fail output.
- State what is trusted and why.
- State what is newly computed.
- Prefer residuals for symbolic identities.
- Prefer comparisons against trusted modules or exact solutions when available.
- Do not validate only that a generated-source string contains fragile
  whitespace or formatting.

Use this workflow when correctness depends on a subtle algorithm, generated
code, a trusted implementation, an exact solution, or a tolerance:

1. Build a test case.
2. State what is trusted and why.
3. Run the new calculation.
4. Compare new output against the trusted result.
5. Print the error, tolerance, and pass/fail result.

Validation requirements by type:

- Symbolic validation must print a residual, identity, or component comparison.
  Tensor checks must cover all relevant independent components.
- Generated-code validation must inspect a complete artifact or parsed metadata
  tied to the generated artifact named in the lesson.
- Numerical validation must print norm type, resolutions, errors, expected
  order, measured order, tolerance rationale, and pass/fail result.
- Project validation must print generated-file inventory, build or run result,
  runtime diagnostics, and final correctness check.

For numerical comparisons, explain the tolerance in plain language. For
convergence tests, print the resolutions, errors, expected order, measured
order, and pass/fail result.

## Execution, Conversion, and Stored Output State

Active executable notebooks must be checked from a fresh kernel with:

```bash
python helpers/execute_notebooks.py --inplace <notebook.ipynb>
```

After execution, run:

```bash
git status --short
```

Review tracked-file changes and untracked generated artifacts. Only keep files
intentionally produced by the change.

Rules:

- Stored outputs must come from one fresh restart-and-run-all execution.
- Execution counts and outputs should not be a mixture of old and new runs.
- Stored outputs must contain no warnings, tracebacks, or environment-repair
  messages.
- External kernel-launch warnings belong in the execution harness, not in
  learner-facing notebook cells.
- Do not add notebook cells solely to repair CI, cache, home-directory, or path
  problems.
- If a notebook intentionally leaves outputs cleared, document that exception in
  the same notebook family README or review policy.

### `helpers/converter.py` Workflow

`helpers/converter.py` is useful for inspection and text editing, but it is
lossy. It drops outputs, execution counts, notebook metadata, and cell metadata
when converting notebooks to percent scripts and back.

Use it this way:

```bash
python helpers/converter.py <notebook.ipynb> <scratch-or-review.py>
python helpers/converter.py <scratch-or-review.py> <notebook.ipynb>
python helpers/execute_notebooks.py --inplace <notebook.ipynb>
```

Rules:

- Use converter output for review or editing workflow only.
- Do not leave generated `.py` conversion artifacts unless they are
  intentionally tracked source.
- Any notebook round-tripped through the converter must be re-executed before
  final review.
- Do not use converter round trips as proof that stored outputs or metadata were
  preserved.
- Inspect the final `.ipynb`, not only the percent script, before merging.

## Plots, Images, and Media

Visual evidence must be reproducible and interpretable.

Rules:

- Numerical-methods notebooks should use visual evidence when it clarifies a
  comparison or trend.
- Good candidates include wave-profile plots, convergence-history plots,
  coordinate-map plots, stencil-weight plots, and diagnostic-error plots.
- Plots must have axis labels, a title, and a legend when multiple curves or
  data sets appear.
- The markdown before a plot must say what comparison, trend, or physical
  behavior the plot is meant to demonstrate.
- A stored object repr such as `<Figure size ...>` is not sufficient evidence;
  the actual rendered plot or image must be stored.
- Images or animations must be produced by notebook code or clearly sourced.
- If an animation is embedded, provide a still frame or textual summary of the
  quantitative result it demonstrates.

## Scientific Provenance and References

Physics-heavy and numerical-methods notebooks should cite models, equations,
methods, and external references where they first matter.

Put references near the relevant concept, not only at the end. Keep reference
text short and use it to support the physics or numerical method, not to replace
missing explanation.

Cite or link on first serious use of:

- named equations and physical models;
- exact solutions and initial-data families;
- coordinate systems and transformations;
- numerical methods such as Method of Lines or finite differences when external
  background is assumed;
- validation concepts such as relative error or convergence order;
- external packages such as SymPy when they are conceptually important.

Good:

```markdown
We pose the wave equation as an initial-value problem: the initial data are
specified at `t = 0`, and the Method of Lines advances the fields forward in
time.
```

## Markdown, Links, Tone, and Exercises

Markdown should be readable as a lesson, not only as technical notes.

Rules:

- Split dense paragraphs.
- Place equations near the definitions they rely on.
- Use monospace for code identifiers, parameters, filenames, and commands.
- Keep tables narrow enough to read in a notebook.
- Link text should describe the target task or concept, not just "here."
- Links must resolve to existing notebooks, source files, documentation, or
  references.
- Avoid hype, jokes, vague motivational prose, and overcompressed API-reference
  prose.
- Avoid saying "obvious" or "trivial" about physics, numerical analysis, or
  generated code.
- Avoid compact API-reference prose. Warning signs include long option lists
  without examples, function names before use cases, parameter lists without
  physical or generated-code roles, and module tours with no visible output.

Exercises should reinforce the workflow just taught.

Exercise rules:

- Keep exercises concrete and close to the preceding material.
- Prefer prompts that ask the learner to change a parameter, complete a loop,
  verify an identity, measure a slope, or explain an output.
- Use a prediction prompt before code when the learner should anticipate a
  result, cancellation, output shape, or convergence trend.
- Use a reflection prompt after code when the learner should explain why the
  output proves the point.
- Provide hints when the exercise depends on a specific data structure.
- Do not turn a first-pass tutorial into a long homework set.
- Do not introduce unrelated new concepts in exercises.

## Specialized Overlay: `c_codegen()`

When teaching `c_codegen()`, follow this sequence:

1. Begin from a simple SymPy expression or NRPy indexed expression.
2. Generate direct C output.
3. Show what common subexpression elimination changes.
4. Show SIMD or finite-difference-aware output only after defining those terms.
5. Print complete generated code for the example being taught.
6. Explain generated variables, temporaries, memory reads, and assumptions.

Define CSE as common subexpression elimination before using the acronym. Define
SIMD as single instruction, multiple data before using the acronym.

## Specialized Overlay: `CFunction` and `register_CFunction()`

Before the first `register_CFunction()` example, show the C function structure:

```c
/*
 * Description of what the function computes.
 */
return_type function_name(parameter_list) {
    local_declarations;
    assignments_or_algorithm;
}
```

Then map C-function pieces to NRPy:

- description comment: `desc`;
- return type: `cfunc_type`;
- function name: `name`;
- parameter list: `params`;
- header dependencies: `includes`;
- code before the function: `prefunc`;
- function body: `body`;
- code after the function: `postfunc`;
- output subdirectory: `subdirectory`;
- coordinate wrapper: `CoordSystem_for_wrapper_func`;
- CodeParameter header: `include_CodeParameters_h`;
- SIMD/intrinsics choice: `enable_simd`.

Teaching sequence:

1. Show the desired concrete C-function shape.
2. Define each Python registration component.
3. Generate or assemble `body`.
4. Register the function using the appropriate pattern.
5. Inspect or validate the complete registered function in a separate cell.

Silent registration is not evidence. A registration helper may be output-free
only if a later cell calls it and prints or validates the complete registered
function or relevant metadata.

## Specialized Overlay: BHaH CFunction Registration

BHaH infrastructure registrations are performed inside registration/helper
functions. A tutorial that claims to follow BHaH practice must follow the same
shape.

Required invariants:

- Use a helper named `register_CFunction_<purpose>()` unless the surrounding
  notebook already has a more specific established naming pattern.
- Define registration pieces as local Python variables before the
  `register_CFunction()` call.
- Assemble or generate `body` before registration.
- Keep tutorial inspection, prints, dictionary resets, and validation outside
  the helper.
- Call the helper in a separate tutorial cell.
- Print or validate the complete registered function or complete relevant
  metadata after the helper call.

Forbidden inside a BHaH-style registration helper:

- `CFunction_dict.pop(...)`;
- debugging prints;
- stored-object inspection;
- tutorial-only validation;
- unrelated registry resets.

Observed BHaH keyword-order families:

- Common project form:
  `subdirectory` when present, `includes`, `prefunc` when present, `desc`,
  `cfunc_type`, `name`, `params`, `include_CodeParameters_h` when explicit,
  `body`, `postfunc` when present.
- Coordinate-wrapper form:
  may place `include_CodeParameters_h` and `CoordSystem_for_wrapper_func`
  earlier, matching nearby BHaH infrastructure files that use coordinate
  wrappers.
- Simple helper form:
  may omit `subdirectory`, `prefunc`, `postfunc`, `CoordSystem_for_wrapper_func`,
  or `enable_simd` when those fields are not relevant.

Tutorials must imitate the closest live BHaH family for the concept being
taught. Do not invent a tutorial-only order and call it BHaH practice.

Option decisions:

- `include_CodeParameters_h=True`: use only when the body reads CodeParameters
  or generated code needs that header.
- `subdirectory`: use only when generated files belong in a project
  subdirectory.
- `prefunc`: use only when helper C definitions must appear before the
  function.
- `postfunc`: use only when helper C definitions must appear after the function.
- `CoordSystem_for_wrapper_func`: use only for coordinate-system wrappers.
- `enable_simd`: use only for SIMD or intrinsic-specific generation.

Tensor or Christoffel examples must show the actual complete parameter list in
the notebook, not a placeholder signature. If the function flattens tensor
components into an output array, state the mapping from tensor indices to flat
offsets before registration.

## Specialized Overlay: Finite Differences and Gridfunctions

Finite-difference tutorials must connect stencils, derivative notation, and
memory access.

Rules:

- Define derivative notation before parsing variable names such as `u_dD0`,
  `u_dDD01`, or `gammaDD_dD012`.
- Explain stencil width, finite-difference order, and upwind/downwind shifts
  before printing coefficients.
- When showing a matrix used to compute coefficients, say what rows and columns
  mean.
- When registering gridfunctions, state the group, rank, dimension, and whether
  names represent base names or full component names.
- When printing memory access strings, say which infrastructure convention is
  being shown.
- If a helper discovers derivative variables automatically, print the complete
  discovered set and explain what each part of the name encodes.

## Specialized Overlay: Start-to-Finish Projects

Workspace rules:

- Use `project/<notebook_slug>` under the notebook directory by default.
- Use a printed temporary directory only for disposable artifacts that are not
  part of the lesson's stable generated project.
- Do not leave absolute user-local paths in stored outputs.
- State whether an existing generated directory is cleaned, reused, or updated
  in place before writing files.
- Print the project path before writing generated files.
- Preserve user edits unless the notebook explicitly owns and regenerates the
  project directory.

Artifact rules:

- Print or list all key generated files.
- Explain build and run commands in terminal-ready blocks when the learner must
  leave Jupyter.
- For Einstein Toolkit notebooks, define thorn, CCL, schedule, interface, and
  parameter files before using those terms.
- Separate code generation, project construction, build/run instructions, and
  validation into distinct sections.
- Do not hide generated project effects in silent cells; follow with file
  listings, checks, or printed paths.

## Pass/Fail Review Checklist

Use this as the final review sheet. Any blocker failure must be repaired or
documented as an explicit exception.

### Archetype and Opening

- Pass: One primary archetype is clear and the notebook follows that contract.
- Pass: Specialized overlays are applied where relevant.
- Pass: Title, author/authors, run-all instruction, purpose, and sequence links
  are present when required.
- Pass: `Notebook Status` and `Validation Notes` appear for physics,
  numerical-methods, and start-to-finish notebooks.
- Blocker: The notebook has no clear learning goal or violates its primary
  archetype.

### Grounding

- Pass: `Words for This Notebook` or `Notation and Terms` is present when
  required.
- Pass: Main variables, physical meanings, notation, and artifact roles appear
  before use.
- Pass: Tensor examples start from indexed notation and map indices to NRPy
  lists or loops.
- Pass: Physics notebooks state the full initial-value problem before
  implementation.
- Blocker: Code introduces terms, variables, or infrastructure objects before
  explaining where they fit.

### Code and Outputs

- Pass: Long code cells are framed with skim/study guidance.
- Pass: Nontrivial code cells have visible evidence or are immediately
  verified.
- Pass: Required evidence outputs are complete and not truncated, excerpted,
  ellipsis-abbreviated, collapsed, or stale.
- Pass: Dense outputs have an inspection checklist.
- Pass: Object-only display reprs are not used as evidence.
- Blocker: A required evidence output is truncated or hidden.

### Generated Artifacts

- Pass: Generated source is complete when source structure is the concept.
- Pass: Generated artifacts answer an inspection question and are followed by
  validation, comparison, or interpretation.
- Pass: Catalogs are used when learners must compare named parameters,
  coordinate systems, gridfunctions, infrastructures, generated files, C
  functions, methods, or test cases.
- Pass: File-writing notebooks print workspace/project paths and generated
  artifacts.
- Blocker: File generation occurs silently or generated artifacts cannot be
  matched to their roles.

### Validation

- Pass: Computed, generated, file-writing, or numerical notebooks have a named
  validation section.
- Pass: Validation fails loudly.
- Pass: Validation states what is trusted and what is newly computed.
- Pass: Symbolic, generated-code, numerical, and project validations meet their
  type-specific requirements.
- Pass: Numerical comparisons explain tolerances and convergence expectations.
- Blocker: A notebook computes, generates, writes, or runs something without
  validating the result.

### Execution and Conversion

- Pass: Notebook executes cleanly from a fresh kernel using
  `helpers/execute_notebooks.py`.
- Pass: `git status --short` after execution contains only intentional changes.
- Pass: Stored outputs contain no warnings, tracebacks, stale execution state,
  or learner-facing environment repair messages.
- Pass: Any notebook round-tripped through `helpers/converter.py` was
  re-executed and reviewed as `.ipynb`.
- Blocker: Converter use erased outputs or metadata and the notebook was not
  re-executed.

### Links and Specialized Overlays

- Pass: Links are current and point to existing notebooks, source files,
  documentation, or references.
- Pass: Scientific provenance appears near first use of named equations,
  physical models, exact solutions, coordinate systems, numerical methods, or
  validation concepts.
- Pass: C-function examples first explain C-function structure.
- Pass: BHaH-style registration examples use a helper function, local
  registration variables, live-practice keyword ordering, and a separate
  inspection/validation cell.
- Pass: Finite-difference examples define derivative notation, stencil width,
  order, gridfunction roles, and memory access before generated output.
- Pass: Plots have labels, titles, legends when needed, and explanatory
  framing.

## Audit Basis

This guide is based on inspection of the frozen canonical tutorial corpus in
`orig_tutorial/`, equivalent to commit
`33ed50470f9c08a21d5daa5ad0dda5b419302fd5`:

- `orig_tutorial/index.ipynb`
- `orig_tutorial/1-intro/c_codegen.ipynb`
- `orig_tutorial/1-intro/c_function.ipynb`
- `orig_tutorial/1-intro/core_infrastructure_etlegacy.ipynb`
- `orig_tutorial/1-intro/finite_difference.ipynb`
- `orig_tutorial/1-intro/grid.ipynb`
- `orig_tutorial/1-intro/how_NRPy_computes_finite_difference_coeffs.ipynb`
- `orig_tutorial/1-intro/indexedexp.ipynb`
- `orig_tutorial/1-intro/params.ipynb`
- `orig_tutorial/1-intro/reference_metric.ipynb`
- `orig_tutorial/1-intro/start_to_finish__finite_difference.ipynb`
- `orig_tutorial/1-intro/ten_minute_overview.ipynb`
- `orig_tutorial/1-intro/wave_equation_with_numpy.ipynb`
- `orig_tutorial/2-basic_physics_applications/start_to_finish__carpet_wavetoy_thorns.ipynb`
- `orig_tutorial/2-basic_physics_applications/start_to_finish__wave_equation_cartesian.ipynb`
- `orig_tutorial/2-basic_physics_applications/wave_equation_and_c_codegen.ipynb`

Recurring patterns preserved:

- title, author, purpose, source links, and table of contents at the top;
- numbered steps with back-to-top navigation;
- problem statement before implementation;
- equations mapped explicitly to NRPy data structures;
- visible output after meaningful code;
- generated C and project artifacts treated as evidence;
- validation notes, residuals, convergence tests, or trusted-module comparisons;
- exercises that ask learners to modify or verify the demonstrated workflow.

Legacy conflicts intentionally not preserved:

- old `../edit/...` source links;
- silent concept-bearing cells;
- very long project-generation cells without enough framing;
- absolute user-local paths in stored output;
- object-only plot/image reprs;
- abbreviated or ellipsis-based outputs;
- PDF/export cells unrelated to the lesson.
