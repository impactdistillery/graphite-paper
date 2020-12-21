.. role:: icon-folder
   :class: fa fa-folder-open

Theme configuraion
==================

You can configure your theme by adding custom styles or tweak template files.

Adding custom styles
---------------------


Using CSS
^^^^^^^^^

The stylesheet, the paper uses is defined in :file:`config/meta.yaml`.

.. code-block:: yaml

    styles:  theme/styles/sample-journal.css

Adjust the stylesheet according to your needs or start with a blank stylesheet.
You can also overwrite the theme's styles by importing the theme stylesheet with `@import` into a custom.css that is be loaded by :file:`meta.yaml`.


Changing SASS
^^^^^^^^^^^^^

If you want to adapt the theme provided by the sample-jounal, you might want to load all SASS files and build up a custom theme.

.. todo::

    - Add SASS structure, list bootstrap version and Icon Version and add watch commands



Overwrite template files
-------------------------

To adjust graphite's html templates that define the navigation or template partials such as the article top, you can overwrite these files by adding them to your custom journal folder.

The file structure neets to follow this pattern:

:icon-folder:`\ ` **graphite/jinja2/**

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

:icon-folder:`\ ` ``_YOUR_ROOT_FOLDER_/jinja2/``

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





