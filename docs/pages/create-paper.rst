.. role:: icon-folder
   :class: fa fa-folder-open

***********************
Create a Graphite paper
***********************

The easiest way to start you graphite paper is to download our sample journal starter.

Download  starter
=================

.. code:: shell

    $ git clone github.com/crosssenses/sample-journal

This will give you a starter with the following pape structure:

:icon-folder:`\ ` ``sample-journal/``

::

    sample-journal
    │
    ├── sample-paper
    │   ├── assets
    │   │   ├── figures
    │   │   ├── images
    │   │   └── csv
    │   │
    │   ├── config
    │   │   ├── development.py
    │   │   ├── lang.yaml
    │   │   ├── meta.yaml
    │   │   └── meta.yaml
    │   │
    │   ├── pages
    │   │   ├── about.md
    │   │   ├── directories.md
    │   │   ├── editors.md
    │   │   ├── index.md
    │   │   └── referenceds.yaml
    │   │
    │   ├── theme
    │   │   ├── fonts
    |   │   │   └── ...
    │   │   ├── images
    |   │   │   └── graphite.svg
    │   │   └── styles
    |   │       └── sample-journal.css
    │   │
    │   └── manage.py
    │
    ├── .gitignore
    │
    ├── Pipfile
    │
    ├── Pipfile.lock
    │
    └── README.md


Add meta information
====================

All meta information and some settings are added in :file:`config/meta.yaml`.

.. include:: meta.rst


Add page content
================

To add content to your publication, edit or create :file:`pages/index.md`.
Pages are written in Markdown with additional, *graphite*-specific syntax for components.

Markdown for text
-----------------

Blank lines divide logical blocks (e.g. paragraphs including asides).

Example for markdown:

.. code-block:: md

    # Markdown

    This an **bold** example with a bullet list:

    * one
    * two
    * three

Further resources on markdown

-  https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet
-  https://guides.github.com/features/mastering-markdown/
-  https://github.github.com/gfm/


Graphite specific plugins and markup
------------------------------------

The content of your publication can be enhanced by the following type of components:

* :ref:`Marginal component`
* :ref:`Inline component`
* :ref:`Container component`
* :ref:`Full-width component`

Additional pages/tabs
---------------------

To create additional pages, add Marktdown files to :file:`pages/SOME_PAGE_SLUG.md` and add tab title and page slug in :file:`config/meta.yaml`.


Add directories
---------------

To add inline literature refences, create a reference list :file:`pages/references.yaml` and use the inline component :ref:`Reference`.
The list of references can be


