# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.1.0] - 2026-03-16

### Added
- **Full internationalisation (i18n) support** — All user-facing strings (e.g. "Collapse", "Expand", "Share", "Download", "Translation", "Original version") are now configurable via `lang.yaml`, with English fallbacks for backward compatibility. A new `lang.yaml.example` template is included. (#41)
- **Dynamic infobox marginals** — `INFOBOX` now renders every non-reserved top-level YAML key as a marginal (class `ms-aside-{slug}`). Both scalar and list values are supported, with full Markdown rendering. Legacy `file_url` / `file_label` usage is preserved. (#43)
- **Markdown & inline-reference rendering in aside templates** — The `markdown` filter is now applied to `authorDescription` and `sourceDescription` fields in `quote_aside.html`, `video_aside.html`, and `author_aside.html`, enabling formatted text and `[: REFERENCE | … :]` inline references in those fields. (#45)
- **`LISTOFREFERENCES` inline include syntax** — A new `[: LISTOFREFERENCES | embed=fragment :]` inline tag can be placed inside any Markdown body (including inside an `INFOBOX` body after `---`). `embed=fragment` omits the outer module wrapper so the reference list integrates cleanly into surrounding content; `embed=module` (default) reproduces legacy standalone behaviour. (#47)
- **`append_to_last_p` Jinja2 filter** — Injects HTML content inside the closing `</p>` of the last paragraph in a string; used internally to attach URL icons to reference entries without embedding HTML in Python code. (#47)
- **`ExternalLinksExtension` Markdown extension** — A custom `markdown.treeprocessors.Treeprocessor` automatically adds `target="_blank" rel="noreferrer noopener"` to every external link (those whose `href` starts with `http://` or `https://`) in author-written Markdown pages. Relative links, anchor links, and `mailto:` links are unaffected. No new runtime dependency required. (#50)
- **Comprehensive translation documentation** — New `docs/pages/translation.rst` documents all supported `lang.yaml` keys, usage examples, and how to add new language strings. (#41)
- **LISTOFREFERENCES embed documentation** — `docs/pages/components.rst` documents the inline include syntax and `embed` parameter with examples. (#49)

### Changed
- **Infobox marginals refactored** — `InfoboxPlugin` now passes the full data dict to the template for dynamic iteration; the `lang` variable is also passed for translation support. (#43)
- **`render_template()` updated** — `AbstractPlugin.render_template()` now calls `_inline_replace()` on Markdown output so that inline references inside plugin body text are resolved correctly. (#45)
- **External link attributes standardised across templates** — `nav.html`, `author_aside.html`, `listofreferences.html`, `infobox_aside.html`, and `report.html` all now consistently carry `target="_blank" rel="noreferrer noopener"` on external links and use properly quoted `href` attributes. (#50)
- **Typographic improvements** — User-facing default strings use typographically correct apostrophes (U+2019) and quotation marks. (#41)

### Fixed
- **Collapsing marginals beside list elements** — Corrected a layout bug where marginal elements adjacent to list items collapsed unexpectedly. (#39)
- **`TypeError` in `YamlPlugin.process()`** — Calling `process()` with an empty config string no longer raises `TypeError: argument of type 'NoneType' is not iterable`. (#47)
- **`TypeError` for `None` values in infobox template** — Added `{% if link %}`, `{% if data %}`, `{% if l %}`, and `l is string` guards so `None` values and non-string elements are skipped gracefully. (#43)
- **Hardcoded German strings removed from templates** — `quote.html`, `quote_aside.html`, `variable_aside.html`, and `author_aside.html` replaced hard-coded "Übersetzung", "Originalversion", and "TEILEN" with `lang.get()` calls with English fallbacks. (#41, #45)
- **`figure_aside.html` lang key corrected** — Renamed `downloadData` → `download_data` to match the documented key name. (#41, #45)
- **Duplicate `{% if author %}` block removed** — `video_aside.html` had a redundant conditional block that has been cleaned up. (#45)

## [1.0.0] - 2025-10-01

This marks the first stable release of Graphite Paper. The framework has been in active development and production use since 2017, powering numerous academic and policy publications.

### Added
- Comprehensive changelog documenting project history
- VERSION file for clear version tracking
- Semantic versioning commitment
- Enhanced documentation for versioning and release process

### Changed
- Version bumped from 0.0.6 to 1.0.0 to mark stable release
- Documentation updated to reflect maturity and stability

### Fixed
- Removed outdated references to colon-based bolding in glossary documentation

## [0.0.6] - 2020-11-13

The initial working release of Graphite Paper, establishing the core framework for digital academic publications.

### Major Features Since Initial Release (Nov 2020 - Sep 2025)

#### Core Publication Features
- **Multi-media publication framework** - Infrastructure for enhanced digital publications combining Django, Jinja2, and Markdown
- **Static site generation** - Build command to generate deployable HTML publications
- **Development server** - Live preview with Django runserver
- **Cookiecutter starter templates** - Easy project initialization

#### Content Components
- **Marginal components** - Pull quotes, key statements, and contextual information displayed in margins
- **Container components** - Structured content blocks (videos, tables, quotes, infoboxes, etc.)
- **Inline components** - References, glossary terms, and cross-references
- **Chapter navigation** - Multi-tab publications with smooth scrolling and deep linking
- **Table of contents** - Automatic generation with configurable depth
- **Named heading IDs** - Custom anchor IDs for precise linking

#### Media & Interactive Elements
- **Video embeds** - Support for YouTube, Vimeo, and TikTok with privacy-friendly options
- **Image galleries** - Carousel and slideshow components
- **Data visualization** - CSV tables with header rows/columns and download functionality
- **Figure thumbnails** - Optimized image loading
- **Popover notes** - Interactive tooltips and annotations

#### Styling & Theming
- **CSS customization** - Comprehensive theme configuration
- **Responsive design** - Mobile-optimized layouts with adaptive marginal content
- **Custom fonts and icons** - Material Design icons integration
- **Social sharing** - Customizable share buttons for multiple platforms

#### Internationalization & Accessibility
- **Multi-language support** - Content translation with language navigation
- **Structured data** - Google Scholar metadata for academic discoverability
- **DOI integration** - Digital Object Identifier support
- **Citation management** - Automatic citation formatting and reference lists

#### Technical Enhancements
- **Build optimization** - Fast static file generation
- **Asset management** - Automatic collection and optimization of static resources
- **JavaScript features** - Tab switching, hash navigation, scroll spy, and modal interactions
- **Bootstrap integration** - Fixed conflicts between modals and carousels
- **Windows compatibility** - Installation instructions for Windows users

#### Bug Fixes & Improvements (2021-2025)
- Fixed glossary colon-based bolding causing parsing errors (Sep 2025)
- Fixed TOC building with anchor link reloads (Sep 2025)
- Added TocDepth variable for TOC customization (Sep 2025)
- Implemented customizable social share platforms (Aug 2025)
- Added named heading IDs with backward compatibility (Aug 2025)
- Fixed JavaScript tab/carousel conflicts (Feb 2023)
- Added collapsible infobox boolean feature (Feb 2023)
- Fixed share button display in figures (Mar 2023)
- Added file download feature to infobox (Mar 2023)
- Fixed scrolling and linking across tabs (Jul 2021)
- Enabled Markdown rendering in license field (Jul 2021)
- Added popover functionality (Jul 2021)
- Optimized internal hash link navigation (Jul 2021)
- Fixed video module bugs (Nov 2021)
- Added thumbnail support for figures (Nov 2021)
- CSV plugin newline rendering (Feb 2022)
- Optional download button (Jan 2024)
- Video URL list functionality (Dec 2023)

### Documentation Improvements
- Comprehensive ReadTheDocs documentation
- Component usage examples and syntax reference
- Theme configuration guide
- Getting started tutorials
- Contribution guidelines
- Windows installation instructions
- Cheatsheet for Google Docs to Markdown conversion

### Notable Publications Created with Graphite Paper
- GDHRNet Working Papers series (4 papers)
- Freedom of Expression in the Digital Public Sphere
- Disclosure Rules for Algorithmic Content Moderation
- Increasing fairness in targeted advertising
- Explainable AI Report
- Plattforminnovation im Mittelstand
- The Strategic Guide to Responsible Platform Business
- Scholar-led Publishing Manifesto

## [0.0.5] and Earlier

Development versions leading to the first working release (v0.0.6). These versions established the basic package structure and Django integration.

---

## Release Process

Graphite Paper follows [Semantic Versioning](https://semver.org/):

- **MAJOR version** (x.0.0): Incompatible API changes
- **MINOR version** (0.x.0): New functionality in a backward compatible manner
- **PATCH version** (0.0.x): Backward compatible bug fixes

## Links

- [PyPI Package](https://pypi.org/project/graphite-paper/)
- [Documentation](https://graphite-paper.readthedocs.io/)
- [GitHub Repository](https://github.com/impactdistillery/graphite-paper)
- [Academic Publication - Theoretical Basis](https://2017.xcoax.org/pdf/xCoAx2017-Hebing.pdf)

[1.1.0]: https://github.com/impactdistillery/graphite-paper/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/impactdistillery/graphite-paper/compare/v0.0.6...v1.0.0
[0.0.6]: https://github.com/impactdistillery/graphite-paper/releases/tag/v0.0.6
