from __future__ import annotations

from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "mapping" / "curriculum_map.yaml"
EXPERIMENTS = ROOT / "mapping" / "experiment_registry.yaml"

VALID_LEVEL_STATUS = {"public_main", "local_uncommitted", "planned"}
VALID_EXPERIMENT_STATUS = {"public_main", "local_uncommitted", "planned", "mixed"}

def load_yaml(path: Path) -> dict:
    with path.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)
    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a mapping at the top level")
    return data

def validate() -> list[str]:
    errors: list[str] = []
    curriculum = load_yaml(CURRICULUM)
    registry = load_yaml(EXPERIMENTS)

    levels = curriculum.get("levels", [])
    experiments = registry.get("experiments", [])
    experiment_ids = {item.get("id") for item in experiments}

    seen_levels: set[str] = set()
    for item in levels:
        level_id = item.get("level_id")
        if level_id in seen_levels:
            errors.append(f"duplicate level_id: {level_id}")
        seen_levels.add(level_id)

        if item.get("status") not in VALID_LEVEL_STATUS:
            errors.append(f"{level_id}: invalid status {item.get('status')!r}")
        if not item.get("book_chapters"):
            errors.append(f"{level_id}: no book chapter mapping")
        for exp_id in item.get("experiments", []):
            if exp_id not in experiment_ids:
                errors.append(f"{level_id}: unknown experiment {exp_id}")

    seen_experiments: set[str] = set()
    for item in experiments:
        exp_id = item.get("id")
        if exp_id in seen_experiments:
            errors.append(f"duplicate experiment id: {exp_id}")
        seen_experiments.add(exp_id)

        if item.get("status") not in VALID_EXPERIMENT_STATUS:
            errors.append(f"{exp_id}: invalid status {item.get('status')!r}")
        if not item.get("chapters"):
            errors.append(f"{exp_id}: no chapter mapping")
        if not item.get("outputs"):
            errors.append(f"{exp_id}: no declared outputs")

    return errors

def main() -> int:
    errors = validate()
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        return 1
    print("Mapping validation passed.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
