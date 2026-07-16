# Internal development workflow

This document is for manuscript authors and maintainers.

## Separation of responsibilities

1. **Learner-facing text** uses readable level and experiment names. It does not expose
   raw commit hashes or internal IDs unless they are pedagogically necessary.
2. **Reproducibility metadata** lives in `mapping/`, `figures/manifest.yaml`, and
   `docs/public/reproducibility.md`.
3. **Git history** records update history. Do not add per-update notes such as
   `CH06_UPDATE_NOTES.md` or one-time Codex prompts to the repository.

## Safe update cycle

```bash
git status
git add .
git commit -m "Checkpoint before manuscript update"
```

Apply the update, then run:

```bash
python scripts/validate_mapping.py
pytest -q
```

Compile the affected edition before committing it.

## Authoring sequence

The evidence-first writing order is:

1. Chapter 6 — phase and interference
2. Chapter 2 — one result versus a distribution
3. Chapter 9 — classical mixture versus entanglement
4. Chapter 11 — Deutsch algorithm
5. Chapter 12 — noise and error

Introductory chapters can then be polished around this tested progression.

## Figure and data pipeline

Use:

```text
tested simulator -> generated data -> figure script -> PDF/SVG -> LaTeX
```

Do not type simulation-derived values directly into LaTeX. Record stochastic seeds,
shot counts, and source functions in `figures/manifest.yaml`.

## SDK isolation

Qiskit and Cirq are optional SDK-lab dependencies. Do not add them to the core app or
manuscript development requirements. Add separate SDK environment files only when the
SDK labs become executable.
