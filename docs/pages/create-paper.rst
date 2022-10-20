.. role:: icon-folder
   :class: fa fa-folder-open

***********************
Create a Graphite paper
***********************

Create a publication repository
===============================

The easiest way to start your first graphite paper is to use our cookiecutter starter.
If you prefer to start with a full, prefilled sample publication, you can clone our sample journal repository instead.

Create publication with starter
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A documentation of how to install our starter can be found here:

   :ref:`Starter`

This will give you a publication repository with the following page structure:

:icon-folder:`\ ` ``YOUR_JOURNAL_SLUG/``

::

    YOUR_JOURNAL_SLUG
    │
    ├── YOUR_PAPER_SLUG
    │   ├── assets
    │   │   └── images
    │   │   │   └── header.jpg
    │   │
    │   ├── config
    │   │   ├── development.py
    │   │   ├── lang.yaml
    │   │   └── meta.yaml
    │   │
    │   ├── pages
    │   │   ├── index.md
    │   │   ├── imprint.md
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
    ├── Pipfile
    │
    └── README.md


Download  sample journal
^^^^^^^^^^^^^^^^^^^^^^^^

A preview of the sample publication can be seen here: `graphite-paper.netlify.app <https://graphite-paper.netlify.app/>`_

To copy this sample, clone the following repository.

.. code:: shell

    $ git clone github.com/crosssenses/sample-journal

This will give you a publication repository with the following page structure:

:icon-folder:`\ ` ``sample-journal/``

::

    sample-journal
    │
    ├── sample-paper
    │   ├── assets
    │   │   ├── figures
    |   │   │   └── ...
    │   │   ├── images
    │   │   └── csv
    │   │
    │   ├── config
    │   │   ├── development.py
    │   │   ├── lang.yaml
    │   │   └── meta.yaml
    │   │
    │   ├── pages
    │   │   ├── about.md
    │   │   ├── directories.md
    │   │   ├── editors.md
    │   │   ├── index.md
    │   │   └── references.yaml
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

In order to print the full list of references use the directory component :ref:`List of references` below your text or on a seperate page.




