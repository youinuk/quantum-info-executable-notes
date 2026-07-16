# From Bits to Qubits — Manuscript Starter

This repository contains the LaTeX manuscript for:

**From Bits to Qubits: An Executable Introduction to Quantum Information**

The companion app is maintained separately:

<https://github.com/youinuk/quantum-info-learning-lab>

## Current writing focus

The current active writing target is:

```text
Chapter 6 — Phase: Information Hidden from a Direct Measurement
```

This update integrates:

- conceptual figures,
- LaTeX tables,
- natural figure references in the body,
- subsection-level quick checks,
- end-of-chapter exercises,
- initial bibliography entries.

## Recommended Overleaf project

For now, use a small Chapter 6 project in Overleaf:

```text
main_ch06.tex
preamble/
chapters/ch06_phase.tex
figures/generated/
bibliography/references.bib
```

Set the Overleaf main document to:

```text
main_ch06.tex
```

Use pdfLaTeX first.

## Public-facing note

Internal experiment IDs such as `EXP-I01` and commit hashes should not be placed in the learner-facing chapter text. They belong in mapping files, reproducibility notes, or instructor/developer documentation.

## File replacement

This update is intended to overwrite:

```text
chapters/ch06_phase.tex
bibliography/references.bib
README.md
```

It also adds or updates:

```text
figures/generated/
docs/INTERNAL_DEVELOPMENT.md
docs/CH06_REPRODUCIBILITY_MAPPING.md
main_ch06.tex
```
