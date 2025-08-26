# Graphite Paper

**ALWAYS follow these instructions first and fallback to search or additional context gathering only if the information here is incomplete or found to be in error.**

Graphite-paper is a Python framework for creating multi-media and interactive digital publications. It combines Django, Jinja2 templating, and Markdown to generate static HTML publications that can be deployed as websites.

## Working Effectively

### Package Development (Contributing to Framework)

Bootstrap and install the repository for development:

```bash
# Install Python dependencies (Python 3.6+ required)
pip3 install -e .
```

Test package installation:

```bash
python3 -c "import graphite_paper; print('Package imported successfully')"
```

Install documentation dependencies and build documentation:

```bash
pip3 install sphinx sphinx_rtd_theme
cd docs/
make html
```

**Build times**: Documentation builds in ~1 second. Build will complete quickly with some warnings (expected).

### End-User Workflow (Creating Publications)

Install the published package:

```bash
pip3 install graphite-paper
```

Create a new publication using the cookiecutter starter:

```bash
pip3 install cookiecutter
cookiecutter gh:impactdistillery/graphite-starter
cd YOUR_JOURNAL_SLUG/
```

**Note**: If pipenv fails due to Python version mismatch, use system Python directly as shown below.

Start development server for your publication:

```bash
cd YOUR_PAPER_SLUG/
python3 manage.py runserver
```

Build static publication files:

```bash
python3 manage.py build
```

**Build times**: Publication builds complete in <1 second. Output goes to `_build/` directory.

View available Django management commands:

```bash
python3 manage.py help
```

## Repository Structure

```
graphite-paper/
├── graphite_paper/          # Main Python package
│   ├── horst/              # Core publication processing
│   ├── local_django/       # Django management commands and settings
│   └── jinja2/             # Template files
├── docs/                   # Sphinx documentation
├── setup.py               # Package configuration
├── pyproject.toml         # Build configuration
└── README.md              # Basic package info
```

### Publication Project Structure (from cookiecutter)

```
sample-journal/
├── sample-paper/           # Django project
│   ├── manage.py          # Django management script
│   ├── assets/            # Publication assets (images, etc.)
│   ├── config/            # Settings and metadata
│   ├── pages/             # Markdown content files
│   ├── static/            # Static files for Django
│   └── theme/             # CSS and design files
└── Pipfile               # Python dependencies
```

## Validation

### Required Manual Testing After Changes

Always test these complete workflows after making changes to the framework:

1. **Package Installation Test**:
   ```bash
   pip3 install -e .
   python3 -c "import graphite_paper; from graphite_paper.horst import parser"
   ```

2. **Publication Creation Test**:
   ```bash
   cd /tmp
   cookiecutter gh:impactdistillery/graphite-starter --no-input
   cd sample-journal/sample-paper/
   python3 manage.py runserver 8001 &  # Use different port
   sleep 2
   curl -f http://localhost:8001/ > /dev/null && echo "Server OK"
   kill %1
   ```

3. **Build Test**:
   ```bash
   python3 manage.py build
   test -f _build/index.html && echo "Build OK"
   test -f _build/frame.html && echo "Frame OK" 
   test -d _build/static && echo "Static files OK"
   ```

4. **Documentation Test**:
   ```bash
   cd docs/
   make html
   test -f _build/html/index.html && echo "Docs OK"
   ```

### Testing User Scenarios

**CRITICAL**: Always test actual functionality, not just builds. After making changes:

1. **Create a test publication** using cookiecutter
2. **Edit content** in `pages/index.md` 
3. **Run development server** and verify content displays correctly
4. **Build static files** and verify HTML output is correct
5. **Check that assets and styling** are properly included

## Common Tasks

### Django Management Commands

Available in any publication project (`YOUR_PAPER_SLUG/`):

- `python3 manage.py runserver [port]` - Start development server (default port 8000)
- `python3 manage.py build` - Build static publication files
- `python3 manage.py collectstatic` - Collect static files only
- `python3 manage.py check` - Validate Django configuration

### Key Files to Edit

When working on the framework:

- `graphite_paper/local_django/management/commands/build.py` - Build process logic
- `graphite_paper/horst/` - Core publication processing modules
- `graphite_paper/jinja2/` - HTML templates
- `docs/` - Documentation files

### Package Dependencies

Core dependencies from setup.py:
- Django (web framework)
- Jinja2 (templating)
- Markdown (content processing) 
- numpy, pandas (data processing)
- PyYAML (configuration)

## Build Times and Timeouts

**Important**: Unlike many projects, graphite-paper builds are extremely fast:

- Package installation: ~30 seconds
- Documentation builds: ~1 second  
- Publication builds: <1 second
- Development server startup: ~2 seconds

**No special timeout handling needed** - builds complete almost instantly.

## Troubleshooting

### Common Issues

**Pipenv Python version errors**: The cookiecutter starter expects Python 3.8 but works with newer versions. Use system Python directly:
```bash
python3 manage.py runserver  # Instead of pipenv shell
```

**Import warnings**: Syntax warnings in `plugins.py` are expected and can be ignored.

**Static file conflicts**: During build, "found another file" warnings are normal - Django uses the first file found.

### No Testing Infrastructure

**Important**: This repository has no existing test suite. When making changes:

- Test manually using the validation scenarios above
- There are no `pytest`, `flake8`, or `black` tools configured
- No GitHub Actions CI/CD exists (only ReadTheDocs for docs)

## Publication Workflow

Users typically:

1. Install graphite-paper package
2. Create publication with cookiecutter starter  
3. Edit content in `pages/*.md` files
4. Customize styling in `theme/` directory
5. Configure metadata in `config/` files
6. Develop with `python3 manage.py runserver`
7. Build final static site with `python3 manage.py build`
8. Deploy `_build/` directory contents to web server

## Key Concepts

- **Horst**: The core processing engine (in `graphite_paper/horst/`)
- **Publications**: Individual websites/papers created by end users
- **Themes**: CSS and design customization
- **Static Build**: Generates self-contained HTML/CSS/JS for deployment
- **Cookiecutter**: Template tool for creating new publications