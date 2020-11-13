========
 Syntax
========

WORKING FILE:

https://docs.google.com/spreadsheets/d/1bp6Y3C1jGtIH9GvygYurikihPT6EIarLHO20KirznWM/edit#gid=0


First rule
----------

Blank lines divide logical blocks (e.g. paragraphs including asides).

Types of plugins
----------------

**(1) Import external markdown file or plugin**

::

    :--- test.md ---:

or

::

    :--- PLUGIN | config.yaml ---:

**(2) Plugin within the text**

::

    :--- PLUGIN ---:
    param1: abc
    param2: xyz
    param_list:
      - a1
      - b2
      - c3
    :--------------:

**(3) Add one or more paragraph-wide side-notes**

::

    Lorem impsum und so weiter
    :--- NOTE ---:
    First side note
    :--- NOTE ---:
    Second side note
    :------------:

**(4) Add a side note, which is linked to a word (foot-note-style)**

::

    Lorem ipsum [: NOTE | test :] und so weiter
    :--- NOTE | test ---:
    Here we go…
    :-----------------:

--------------

Markdown for text
-----------------

Example:

::

    # Markdown

    This an *markdown* example with a bullet list:

    * one
    * two
    * three

-  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
-  https://guides.github.com/features/mastering-markdown/
-  https://github.github.com/gfm/

Objects are defined as yaml objects
-----------------------------------

::

    Lorem ipsum dolor[: NOTE:test :] sit amet
    sdfasdsd
    :--- NOTE:test ---:
    This is a test note
    :-----------------:

    Or as stand-alone objects:

    :------------------- CODE ----------------------:
    class Test:
        def __init__(self, name):
            self.name = name
    :-----------------------------------------------:

External files
--------------

::

    :--- file.md ---:

    :--- PLUGIN:file.yaml ---:

Marginal notes
--------------

Marginal notes can have multiple origins. They can be extracted from the
markdown (e.g. footnotes or glossary entries) – syntax to be determined.

Marginal notes concerning the entire paragraph can be separated by three
dashes. Example:

::

    This is a paragraph
    :--- NOTE ---:
    First marginal note
    :--- NOTE ---:
    Second marginal note for the same paragraph
    :------------:


References
----------

The Reference to a source in the text consists of a slug to the full reference and the text displayed.

Note: To display reference icons without inline citation just leave the last element blank.

::

    This is text [: REFERENCE | AuthorCoauthor2020 | Author, F., Coauthor, S. 2016 :] that goes on.

And in references.yaml

::

  AuthorCoauthor2020:
      short: "Author, F., Coauthor, S. (2016). Some fancy title, 7(1)."
      long: ""Author, F., Coauthor, S. (2016). Some fancy title, 7(1). 2053951719897945."


Author
----------

::

    :--- AUTHOR ---:
    file: assets/images/authors/….png
    name: Martha Mustermann
    institution: Brand Inc.
    website: https://www.impactdistillery.de/graphite
    linkedinName: sample
    description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    :--------------:


Chapter Header
--------------
::

  # header

or

::

  :----- CHAPTER_HEADER -----:
  image: "assets/images/find-experts-at-kilta-com-k9pmyStHKXE-unsplash.jpg"
  title: Introduction
  subtitle: Design publications with a digital dissemination in mind
  :--------------------------:

