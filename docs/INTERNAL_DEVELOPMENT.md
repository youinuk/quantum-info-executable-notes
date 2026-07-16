# Internal development notes

This file is for project development, not for the public-facing manuscript description.

## Current state

- The companion app has reached Level 12 publicly.
- Chapter 6 is the first sample chapter to make the project style concrete.
- The current Chapter 6 figures are draft figures.
- The current bibliography is an initial working bibliography, not the final literature review.

## File replacement rule

Before applying a new update pack:

```bash
git status
git add .
git commit -m "Save current manuscript state before update"
```

Then copy the update files into the repository.

After copying:

```bash
git status
git diff
```

Then commit again:

```bash
git add .
git commit -m "Apply Chapter 6 integrated update"
```

## README policy

Use two README-like files:

```text
README.md
```

Public-facing project overview.

```text
docs/INTERNAL_DEVELOPMENT.md
```

Private/internal workflow notes, checkpoint policy, and drafting reminders.

## Chapter 6 revision checklist

- Does every figure have an in-text reference before or near the figure?
- Are figure captions explanatory without being too long?
- Does the chapter avoid the phrase "tries all answers and reads the right one"?
- Does the core path remain readable without complex numbers?
- Are complex amplitudes and Bloch-sphere comments confined to optional/deeper material?
- Are all citations present in `bibliography/references.bib`?
- Does Overleaf compile with `main_ch06.tex`?
- Are figure files stored under `figures/generated/`?
