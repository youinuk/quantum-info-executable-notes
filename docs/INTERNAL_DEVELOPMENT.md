# Internal development notes

This file is for internal project development, not for the public-facing manuscript description.

## Current policy

Keep three layers separate:

1. **Learner-facing chapter text**
   - Uses ordinary names: Level 4, Level 11, interference experiment, phase sweep.
   - Does not show internal IDs such as `EXP-I01`.
   - Does not show raw commit hashes.

2. **Instructor/reproducibility notes**
   - May show experiment IDs, function names, app commits, and figure-generation scripts.

3. **Mapping files**
   - Store exact connections among app levels, simulator functions, manuscript figures, and tests.

## Recommended app-side improvement

Add a small teacher/developer metadata panel in the app, or a documentation page such as:

```text
docs/experiment_registry.md
```

Each record can include:

```text
Experiment display name
Internal ID
App level
Simulator function
Page file
Manuscript chapter
Figure files
Test files
```

This makes IDs discoverable without burdening the learner-facing UI.

## Before applying update packs

```bash
git status
git add .
git commit -m "Save current manuscript state before update"
```

After applying an update pack:

```bash
git status
git diff
git add .
git commit -m "Apply Chapter 6 integrated update"
```
