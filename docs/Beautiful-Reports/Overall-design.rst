================
 Overall design
================

Layout
------

-  The standard layout is the multi-layer narrative as described in
   Paper xCoAx.
-  As an alternative, we provide an slide-based layout, similar to the
   concept for the m·stats homepage.

Syntax and file structure
-------------------------

-  We distinguish two types of content
-  Markdown (for text) and
-  Objects (which can be stored in individual files or as part of a
   markdown file) and are described in YAML.
-  There is always a ``main.md`` file.
-  Sub-files can either be markdown files or objects

Objects
-------

-  Objects have a **class** and know **class-inheritance** – e.g., there
   could be an object ``visualization`` with children like ``barplot``
   or ``histogram``.
-  Objects are defined in **YAML**. The parameters available are defined
   by the class.

Three levels
------------

**Frame:** This is the outer frame of the HTML report, including the
heading. The frame provides an overall structure with tabs and contains
a placeholder for the actual article.

**Article:** One of the tabs in the frame contains the article, which is
basically a definition of sub-elements – either plugins (YAML) or text
(Markdown).

**Plugin / module:** Each module has a input definition and returns at
least a content object, most modules return an additional aside object.
Further details for the layout might also be part of the return values.
