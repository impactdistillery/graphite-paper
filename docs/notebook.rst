.. role:: icon-folder
   :class: fa fa-folder-open


Notebook
========

The notebook contains random documentation bits and notes, not yet sorted in to the overall structure.


Overwrite template files
------------------------------------

To adjust graphite's html templates that define the navigation or template partials such as the article top, you can overwrite these files by adding them to your custom journal folder.

The file structure neets to follow this pattern:

:icon-folder:`\ ` :file:`graphite/jinja2/`

::

    jinja2
    │
    ├── base.html
    │
    ├── horst
    │   ├── article_top.html
    │   ├── footer.html
    │   ├── frame.html
    │   │
    │   ├──  plugins
    │   │   ├── article_top_aside.html
    │   │   ├── article_top.html
    │   │   ├── …
    │   │   ├── [plugin]_aside.html
    │   │   ├── [plugin]_pre.html
    │   │   ├── [plugin].html
    │   │   └── …
    │   │
    │   ├── render
    │   │   ├── …
    │   │   ├── full.html
    │   │   ├── section.html
    │   │   ├── single.html
    │   │   ├── three.html
    │   │   ├── two.html
    │   │   └── …
    │   │
    │   ├── report.html
    │   ├── share.html
    │   └── tab_content.html
    │
    └── nav.html


To overwrite one of these templates, create a :file:`jinja2` directory in the root folder of your graphite project next to the individual paper folders.

:icon-folder:`\ ` :file:`_YOUR_ROOT_FOLDER_/jinja2/`

.. admonition:: Example

   To adjust the expanding top navigation

   - copy the content of `graphite/jinja2/nav.html <../../../graphite/jinja2/nav.html>`_
   - paste the content into :file:`_YOUR_ROOT_FOLDER_/jinja2/nav.html` (same level and identical name)
   - and adjust to your fit.

.. Note::

   These adjustments will be applied to all papers in the project folder. Paper-specific adjustments – so far – require individual projects.




.. todo::

    Adapt folder structure once horst is renamed

..
    Pulles code and puts in code block
    .. literalinclude:: ../graphite/jinja2/nav.html





