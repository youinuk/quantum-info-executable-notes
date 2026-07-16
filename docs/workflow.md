# Manuscript workflow

## 1. Freeze an app baseline

After the Level 12 commit:

1. Record the full commit hash in:
   - `mapping/curriculum_map.yaml`
   - `preamble/commands.tex`
   - `README.md`
2. Run the app test suite.
3. Export a content inventory for Levels 0--12.
4. Do not silently change the baseline used for a released manuscript.

## 2. Update mappings after the commit

Replace every `SET_AFTER_LEVEL12_COMMIT` and `TBD_AFTER_COMMIT` value with:

- exact page path,
- exact lesson path,
- simulator function,
- relevant test,
- experiment output,
- figure-generation script.

## 3. Generate publication data

Preferred pipeline:

`tested simulator -> generated CSV/JSON -> figure script -> PDF/SVG -> LaTeX`

Do not type simulation-derived numerical values directly into LaTeX.

## 4. Write in chapter order, publish in evidence order

Recommended first complete chapter: Chapter 6, Phase.

Then complete:

1. Chapter 2: one result versus a distribution,
2. Chapter 9: classical mixture versus Bell state,
3. Chapter 11: Deutsch algorithm,
4. Chapter 12: noise and error.

These chapters establish the project's distinctive learning progression before the
introductory chapters are polished.

## 5. SDK isolation

Maintain separate optional environments:

- `requirements-sdk-qiskit.txt`
- `requirements-sdk-cirq.txt`

The core manuscript and app must compile/run without either SDK.
