# From Bits to Qubits

LaTeX source for **From Bits to Qubits: An Executable Introduction to Quantum Information**.
The intended readers are high-school students, undergraduates, and general readers with
high-school mathematics.

Companion app: <https://github.com/youinuk/quantum-info-learning-lab>

## Build targets

| Purpose | Main file |
|---|---|
| Full lecture-note manuscript | `main.tex` |
| Condensed tutorial/review edition | `editions/review.tex` |
| Chapter 6 working edition | `editions/chapter06.tex` |

For the current Overleaf workflow, set `editions/chapter06.tex` as the main document.
The complete manuscript will later use `main.tex`.

Local commands:

```bash
make validate
make test
make chapter06
make book
make review
```

## Repository structure

```text
main.tex                 primary full-manuscript entry point
editions/                alternate build targets
chapters/                one LaTeX source file per chapter
appendices/              optional mathematical and reproduction material
frontmatter/             abstract, preface, and notation
preamble/                packages, commands, and environments
bibliography/            BibTeX database
figures/generated/       publication figure PDFs used by LaTeX
figures/manifest.yaml    figure status and provenance
mapping/                 curriculum and experiment source-of-truth files
sdk_labs/                optional SDK material, separate from the core path
scripts/, tests/         mapping validation tools
docs/public/             reader-facing technical documentation
docs/internal/           authoring and release workflow
```

## Source-of-truth policy

- App-to-book curriculum mapping: `mapping/curriculum_map.yaml`
- Internal experiment IDs and outputs: `mapping/experiment_registry.yaml`
- Figure files and provenance: `figures/manifest.yaml`
- Mathematical notation: `docs/public/mathematical_conventions.md`
- App baseline and reproducibility: `docs/public/reproducibility.md`

Do not duplicate these registries in chapter prose or temporary Markdown files.
Git history is used for change history; update-specific changelog files are not kept in
the manuscript tree.

## Current status

Chapter 6 is the first developed pilot chapter. Most other chapters and appendices are
structured drafts. Generated build PDFs and LaTeX auxiliary files are not versioned.
