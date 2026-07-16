# From Bits to Qubits — Manuscript Starter

This repository contains the LaTeX manuscript for:

**From Bits to Qubits: An Executable Introduction to Quantum Information**

The companion app is maintained separately:

<https://github.com/youinuk/quantum-info-learning-lab>

## Current manuscript status

This starter is now aligned with:

- app baseline commit: `9f7ef8ecc3853ed966a30e07775ed6e4370e4ffa`
- Level 9--12 addition commit: `b42f0ea729608f7e5b7325d62e4ba6c70b9b8dfa`
- current writing focus: Chapter 6, **Phase: Information Hidden from a Direct Measurement**

## Recommended Overleaf start

For the current writing phase, use the Chapter 6 project rather than uploading the
entire future book.

Upload this minimal structure to Overleaf:

```text
main_ch06.tex
preamble/
chapters/ch06_phase.tex
figures/generated/
bibliography/references.bib
```

Set the main document to:

```text
main_ch06.tex
```

Use pdfLaTeX first.

## Included Chapter 6 update

The integrated Chapter 6 file now includes:

- figure blocks inserted in the body,
- natural in-text references to each figure,
- revised explanation of amplitudes, relative sign, phase, and interference,
- misconception boxes,
- additional exercises,
- instructor/revision notes,
- initial BibTeX citations.

Main files:

```text
chapters/ch06_phase.tex
figures/generated/fig_exp_i01_hh_hzh_result.pdf
figures/generated/fig_exp_i02_amplitude_table.pdf
figures/generated/fig_ch06_recombination_summary.pdf
figures/generated/fig_exp_i03_phase_sweep.pdf
bibliography/references.bib
```

## Longer-term structure

The full manuscript will later include:

```text
main_notes.tex
main_review.tex
frontmatter/
chapters/
appendices/
sdk_labs/
mapping/
figures/
bibliography/
```

For now, keep the Overleaf project small and chapter-focused.

## Suggested workflow

1. Commit the current repository state.
2. Copy this update pack into the repository root.
3. Allow the following files to overwrite older versions:

```text
chapters/ch06_phase.tex
bibliography/references.bib
README.md
```

4. Add the new figure files under:

```text
figures/generated/
```

5. Compile `main_ch06.tex`.
6. Commit the update:

```bash
git add .
git commit -m "Integrate Chapter 6 figures, references, and exercises"
```

## Note on figures

The current Chapter 6 figures are manuscript-draft figures. Before an arXiv or
publication release, regenerate the figures from the fixed app baseline and record
the script, seed, and output files in the figure manifest.
