# Codex instruction: add experiment registry to the app repository

Apply the following changes to the `quantum-info-learning-lab` repository.

## Goal

Add a developer/instructor-facing experiment registry that maps app levels, internal
experiment IDs, page files, simulator functions, manuscript chapters, figure targets,
and status. This registry should not clutter the learner-facing app UI.

## Files to add

Create:

```text
docs/experiment_registry.md
```

Use the content from the attached `docs/experiment_registry.md` file.

## README update

In the main `README.md`, add a short section near the development or documentation
area:

```markdown
## Developer and reproducibility metadata

Internal experiment IDs, app-level mappings, manuscript chapter links, and figure
targets are tracked in:

`docs/experiment_registry.md`

These IDs are for reproducibility and instructor/developer use. They are not required
for learners using the app.
```

## Optional app UI addition

If there is already a Resources or teacher-facing section, add a small link or note:

```text
Developer registry: docs/experiment_registry.md
```

Do not add internal experiment IDs directly into the learner-facing level pages.

## Consistency checks

After adding the file:

1. Confirm that all currently public levels 0--12 are represented.
2. Confirm that the following functions are listed:
   - `simulate_bit_trials`
   - `apply_single_qubit_gate`
   - `independent_two_qubit_distribution`
   - `simulate_two_basis_correlations`
   - `run_deutsch_one_bit`
   - `simulate_noisy_bit_measurements`
   - `simulate_named_circuit`
   - `simulate_measurement_series`
   - `simulate_phase_interference`
   - `simulate_entanglement_limit`
3. Do not add Qiskit or Cirq to the base `requirements.txt`.
4. Keep planned Level 13 and Level 14 entries marked as `planned`.

## Commit message

Use:

```text
Add experiment registry for reproducibility and manuscript mapping
```
