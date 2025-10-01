*********
Changelog
*********

All notable changes to Graphite Paper are documented here.

Version 1.0.0 (2025-10-01)
==========================

**First Stable Release**

This marks the first stable release of Graphite Paper. The framework has been in active development and production use since November 2020, powering numerous academic and policy publications.

Added
-----

* Comprehensive changelog documenting project history
* VERSION file for clear version tracking
* Semantic versioning commitment
* Enhanced documentation for versioning and release process

Changed
-------

* Version bumped from 0.0.6 to 1.0.0 to mark stable release
* Documentation updated to reflect maturity and stability

Fixed
-----

* Removed outdated references to colon-based bolding in glossary documentation

Version 0.0.6 (2020-11-13)
==========================

**Initial Working Release**

The initial working release of Graphite Paper, establishing the core framework for digital academic publications.

Major Features
--------------

Core Publication Features
~~~~~~~~~~~~~~~~~~~~~~~~~

* **Multi-media publication framework** - Infrastructure for enhanced digital publications
* **Static site generation** - Build command to generate deployable HTML publications
* **Development server** - Live preview with Django runserver
* **Cookiecutter starter templates** - Easy project initialization

Content Components
~~~~~~~~~~~~~~~~~~

* **Marginal components** - Pull quotes, key statements, and contextual information
* **Container components** - Videos, tables, quotes, infoboxes, and more
* **Inline components** - References, glossary terms, and cross-references
* **Chapter navigation** - Multi-tab publications with smooth scrolling
* **Table of contents** - Automatic generation with configurable depth
* **Named heading IDs** - Custom anchor IDs for precise linking

Media & Interactive Elements
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* **Video embeds** - YouTube, Vimeo, and TikTok support
* **Image galleries** - Carousel and slideshow components
* **Data visualization** - CSV tables with download functionality
* **Figure thumbnails** - Optimized image loading
* **Popover notes** - Interactive tooltips and annotations

Styling & Theming
~~~~~~~~~~~~~~~~~

* **CSS customization** - Comprehensive theme configuration
* **Responsive design** - Mobile-optimized layouts
* **Custom fonts and icons** - Material Design icons integration
* **Social sharing** - Customizable share buttons

Internationalization
~~~~~~~~~~~~~~~~~~~~

* **Multi-language support** - Content translation with language navigation
* **Structured data** - Google Scholar metadata
* **DOI integration** - Digital Object Identifier support
* **Citation management** - Automatic citation formatting

Notable Bug Fixes (2021-2025)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Fixed glossary colon-based bolding causing parsing errors (Sep 2025)
* Fixed TOC building with anchor link reloads (Sep 2025)
* Added TocDepth variable for TOC customization (Sep 2025)
* Implemented customizable social share platforms (Aug 2025)
* Added named heading IDs with backward compatibility (Aug 2025)
* Fixed JavaScript tab/carousel conflicts (Feb 2023)
* Added collapsible infobox features (Feb 2023)
* Fixed scrolling and linking across tabs (Jul 2021)
* Enabled Markdown rendering in license field (Jul 2021)

Release Process
===============

Graphite Paper follows `Semantic Versioning <https://semver.org/>`_:

* **MAJOR version** (x.0.0): Incompatible API changes
* **MINOR version** (0.x.0): New functionality in a backward compatible manner
* **PATCH version** (0.0.x): Backward compatible bug fixes

Links
=====

* `PyPI Package <https://pypi.org/project/graphite-paper/>`_
* `Documentation <https://graphite-paper.readthedocs.io/>`_
* `GitHub Repository <https://github.com/impactdistillery/graphite-paper>`_
* `Sample Publication <https://graphite-paper.netlify.app/>`_
* `Full Changelog <https://github.com/impactdistillery/graphite-paper/blob/master/CHANGELOG.md>`_
