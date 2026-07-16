# Reproducibility

## Companion app baseline

- Repository: `https://github.com/youinuk/quantum-info-learning-lab`
- Draft baseline branch: `main`
- Draft baseline commit: `9f7ef8ecc3853ed966a30e07775ed6e4370e4ffa`
- Level 9--12 addition commit: `b42f0ea729608f7e5b7325d62e4ba6c70b9b8dfa`

These hashes identify the current drafting baseline. Before a public manuscript release,
replace the drafting reference with a tagged app release and, when available, an archival
DOI.

## Canonical metadata

- `mapping/curriculum_map.yaml` maps app levels to manuscript chapters.
- `mapping/experiment_registry.yaml` maps internal experiment IDs to app code and outputs.
- `figures/manifest.yaml` records figure files, source type, status, and reproducibility data.

Human-readable chapter text should not duplicate raw registries. A registry change must be
made in the canonical YAML file and validated in the same commit.

## Publication figures

Numerical values must come from tested functions rather than hand-entered LaTeX values.
Stochastic figures must record an explicit seed and shot count. Conceptual diagrams must be
identified as conceptual rather than simulator output.

Run:

```bash
python scripts/validate_mapping.py
pytest -q
```

before tagging a manuscript baseline.
