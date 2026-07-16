# Release checklist

## Manuscript

- Compile `main.tex` without unresolved references or citations.
- Confirm that figures and tables are referenced in the text.
- Remove draft placeholders and internal-only comments.
- Review accessibility of captions and notation for the intended audience.

## Reproducibility

- Tag the companion app baseline.
- Replace drafting commit hashes with the release tag and archival DOI when available.
- Validate all curriculum and experiment mappings.
- Confirm figure source, seed, shot count, and output file in `figures/manifest.yaml`.

## Licensing

Choose licenses deliberately for:

- application and simulation code,
- manuscript source and educational text,
- generated figures,
- third-party screenshots, logos, or quoted material.

A common pattern is a permissive software license for code and an appropriate Creative
Commons license for text and original figures, but no license is selected automatically.

## Distribution

Do not commit build PDFs, LaTeX auxiliary files, cache directories, or temporary update
packages. Public source releases should contain only manuscript sources, required figure
assets, bibliography, mappings, tests, and durable documentation.
