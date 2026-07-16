# Next work package after Level 12 commit

## Goal

Turn the now-public Level 0--12 app into a manuscript-ready baseline and start
the first serious chapter draft.

## Work package A — stabilize the baseline

### A1. Create a tag

Recommended tag:

```bash
git tag v0.3.0-curriculum-baseline
git push origin v0.3.0-curriculum-baseline
```

Do this only after local tests pass.

### A2. Run tests

```bash
conda run -n quantum_lab python -m compileall -q app.py core pages tests
conda run -n quantum_lab pytest -q
```

### A3. Add release-facing files

Add or update:

```text
CHANGELOG.md
CITATION.cff
LICENSE
docs/reproducibility.md
docs/mathematical_conventions.md
```

## Work package B — generate publication figures

First generate figures for Chapter 6.

Priority figures:

1. `EXP-I01`: H-H versus H-Z-H
2. `EXP-I03`: phase sweep, bright/dark probability
3. `EXP-ALG01`: Deutsch connection preview
4. `EXP-ENT01`: later cross-reference to Bell-state basis comparison
5. `EXP-STAT01`: measurement statistics for earlier chapter cross-reference

Do not manually enter numerical values in LaTeX. Generate them from simulator functions.

## Work package C — write Chapter 6 first

Recommended first complete chapter:

```text
chapters/ch06_phase.tex
```

Reason:

- It uses Level 4 and Level 11 together.
- It shows the core contribution: probability -> amplitude -> phase -> interference.
- It is understandable to high-school readers but mathematically meaningful.
- It connects naturally to Deutsch without requiring the full algorithm yet.

Chapter 6 target:

- 10--14 manuscript pages
- 5--7 figures/tables
- 6 basic exercises
- 3 optional deeper exercises
- 2 misconception boxes
- 1 bridge box to Deutsch
- 1 bridge box to double-slit or Mach-Zehnder analogy

## Work package D — keep SDK separate

Level 9 includes Qiskit/Cirq read-only examples, but the book should not move into
SDK practice yet. Keep Qiskit/Cirq in `SDK Lab`, not in the core conceptual chapters.
