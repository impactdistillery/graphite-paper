# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

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

[1.0.0]: https://github.com/impactdistillery/graphite-paper/compare/v0.0.6...v1.0.0
[0.0.6]: https://github.com/impactdistillery/graphite-paper/releases/tag/v0.0.6
