# Chapter 6 reproducibility mapping

This file keeps technical mapping information out of the learner-facing chapter text.

## Companion app baseline

- Repository: `https://github.com/youinuk/quantum-info-learning-lab`
- Draft baseline commit: `9f7ef8ecc3853ed966a30e07775ed6e4370e4ffa`
- Level 9--12 addition commit: `b42f0ea729608f7e5b7325d62e4ba6c70b9b8dfa`

For final publication, replace this with a versioned release tag and DOI if available.

## Chapter 6 source levels

| Chapter topic | App source | Internal experiment ID | Simulator/function source |
|---|---|---|---|
| H-H vs H-Z-H | Level 4 | EXP-I01 | `apply_single_qubit_gate` |
| Amplitude/sign comparison | Level 4 / manuscript derivation | EXP-I02 | symbolic derivation |
| Phase sweep | Level 11 | EXP-I03 | `simulate_phase_interference` |
| Deutsch bridge | Level 7 | EXP-ALG01 | `run_deutsch_one_bit` |

## Figure mapping

| Figure file | Role | Source status |
|---|---|---|
| `fig_ch06_hidden_phase_concept.pdf` | Conceptual figure for hidden relative sign | manuscript-generated |
| `fig_ch06_recombination_flow.pdf` | Conceptual figure for recombination | manuscript-generated |
| `fig_ch06_phase_sweep.pdf` | Phase sweep graph | should be regenerated from app baseline before final release |

## Final-release TODO

- Regenerate `fig_ch06_phase_sweep.pdf` from the exact app baseline.
- Record script path and seed.
- Add figure checks to the manuscript repository.
- Replace raw commit hash with release tag and DOI.
