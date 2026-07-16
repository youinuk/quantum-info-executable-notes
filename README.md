# Quantum Information Executable Notes — starter

This is a manuscript starter for:

**From Bits to Qubits: An Executable Introduction to Quantum Information**

Primary readers:

- high-school students,
- undergraduates,
- general readers.

Prerequisite: high-school mathematics.

## Important baseline rule

The public companion repository currently exposes Levels 0--8, while Levels 9--12
were reported as local work awaiting commit when this starter was generated.
After that commit, replace all:

- `SET_AFTER_LEVEL12_COMMIT`
- `TBD_AFTER_COMMIT`

with exact paths, function names, tests, and the full commit hash.

## Main files

- `main_notes.tex`: full lecture-notes/book structure.
- `main_review.tex`: shorter tutorial-manuscript structure.
- `mapping/curriculum_map.yaml`: app Level to book chapter map.
- `mapping/experiment_registry.yaml`: stable experiment identifiers.
- `figures/figure_manifest.yaml`: publication figure plan.
- `docs/mathematical_conventions.md`: normative conventions.
- `chapters/ch06_phase.tex`: first pilot chapter with initial substantive material.

## Build verification

Both `main_notes.tex` and `main_review.tex` were successfully compiled with pdfLaTeX when this starter was generated. The bibliography commands remain commented until the first verified citations are added.

## Overleaf

1. Upload the entire zip to a new Overleaf project.
2. Set the main document to `main_notes.tex` or `main_review.tex`.
3. Use pdfLaTeX initially.
4. Replace `AUTHOR NAME`.
5. Replace the app commit placeholder immediately after the Level 12 commit.

## Local validation

```bash
python scripts/validate_mapping.py
pytest -q
```

Optional local LaTeX build:

```bash
latexmk -pdf main_notes.tex
latexmk -pdf main_review.tex
```

## Separation of responsibilities

- The app provides short explanations, interaction, and immediate feedback.
- The manuscript provides logical connections, derivations, limitations, references,
  misconception analysis, and exercises.
- SDK Labs provide optional Qiskit/Cirq syntax and external execution.
