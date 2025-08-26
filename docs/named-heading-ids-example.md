# Named Heading IDs Example {#example}

This document demonstrates the named heading IDs feature in graphite-paper.

## Introduction {#introduction}

Named heading IDs allow you to create permanent, stable links to specific sections of your document.

### Benefits {#benefits}

- **Permanent links**: Won't break when content is edited
- **Readable URLs**: More meaningful than numeric IDs
- **SEO friendly**: Better for search engines

## Usage Examples {#usage}

### Research Papers {#research-papers}

For academic papers, you might use:

```markdown
# Abstract {#abstract}
## Introduction {#introduction}
## Literature Review {#literature}
## Methodology {#methodology}
## Results {#results}
## Conclusion {#conclusion}
```

### API Documentation {#api-docs}

For technical documentation:

```markdown
# API Reference {#api-reference}
## Authentication {#authentication}
## Endpoints {#endpoints}
### User Management {#users}
### Data Operations {#data}
## Error Handling {#errors}
```

## Backward Compatibility

Headings without named IDs continue to work as before:

```markdown
## Regular Heading
### Another Section
```

These will get automatically generated IDs like `heading-partial-123`.

## Conclusion {#conclusion}

The named heading IDs feature provides a powerful way to create stable, meaningful links while maintaining full backward compatibility with existing documents.