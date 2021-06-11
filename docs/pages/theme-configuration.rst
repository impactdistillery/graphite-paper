.. role:: icon-folder
   :class: fa fa-folder-open

==================
Theme configuraion
==================


.. sidebar:: Create your own journal

   Establish a publication series for your institution or start a magazine – the possibilities are endless. Simply adjust layout and style to fit your needs.


You can configure your theme by adding custom styles and tweaking template files.

The starter pack comes with default CSS styles, that can be adjusted with a custom stylesheet.
For bigger adjustments, a modification of the original SCSS theme might make sense.



Adding custom styles
---------------------


Using CSS
^^^^^^^^^

The stylesheet, the paper uses is defined in :file:`config/meta.yaml`.

.. code:: yaml

    styles:  theme/styles/sample-journal.css

Adjust the stylesheet according to your needs or start with a blank stylesheet.
You can also overwrite the theme's styles by importing the theme stylesheet into a custom stylesheet that is then added to :file:`meta.yaml`.

:icon-folder:`\ ` **theme/styles/custom.css**

.. code:: css

    /*************************************************************+/
    /*                                                            */
    /*         Custom styles for graphite publication             */
    /*                                                            */
    /*************************************************************+/

    // Import sample journal theme
    @import 'sample-journal.css';

    // Add your custom styles below



Create you own theme
--------------------

If you want to create your own theme, you can use the graphite theme starter.

Clone the starter pack:

.. code:: shell

    $ git clone https://github.com/crosssenses/graphite-theme-starter



.. todo::

    - Add SASS structure, list bootstrap version and Icon Version and add watch commands
    - Create starter from sample journal



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





