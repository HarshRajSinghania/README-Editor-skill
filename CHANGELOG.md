# Changelog

All notable changes to this project are documented here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added

- `scripts/check_doc_counts.py`: CI check that documented style, palette and profile-template counts stay in sync with the code (#20).
- `make_banner.py --style pulse`: soft concentric rings breathing behind the title, with dark and light variants (#15, thanks @Sultanast01).

## [1.1.0] - 2026-10-13

### Added

- `make_banner.py --logo FILE`: embeds a PNG, SVG, WebP, JPG or GIF logo in a header, with a soft accent glow so dark logos stay visible on dark banners. Spotlight centres it above the title; other styles place it on the left and keep the title clear of it.
- `ghost` palette (cyan, blue and purple on deep navy), matching the readme-forge logo.
- readme-forge logo, rebranded header, footer and CTA buttons, and a 1280×640 social preview image.

### Changed

- Demo video and GIF: local paths, plan name and installed-plugin list are blurred.

## [1.0.1] - 2026-10-12

### Fixed

- `score_readme.py --hf` crashed on model cards (a regex was split at `|` inside a group).
- `analyze_repo.py` no longer reports env vars, routes and tests from `demo/`, `examples/`, `samples/`, `fixtures/` and `testdata/` as the project's own. They are listed in `example_dirs` instead.
- `make_banner.py` printed absolute paths (`C:/Users/...`) in the README snippet when `--out` was absolute. Paths are now relative to the repository root.

## [1.0.0] - 2026-10-12

### Added

- `readme-forge` skill: project READMEs from real code facts, GitHub profile READMEs (11 archetypes), Hugging Face model/dataset/Space cards, and PyPI/npm/GitLab variants.
- `make_banner.py`: 15 animated SVG banner styles with dark/light variants, footers, dividers and CTA buttons.
- Scoring, analysis and import-graph scripts, all standard-library only.
- Demo sample app and GIF.
