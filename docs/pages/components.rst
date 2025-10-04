.. role:: variable
    :class: guilabel variable

.. role:: syntax
    :class: guilabel syntax

**********
Components
**********

.. _Marginal component:

Marginal component
==================

.. sidebar:: Enhanced narrative

   Marginal components are displayed next to a paragraph (or above on mobile). They complement the main narrative with key statements or additional information and explanations.

A marginal component follows the paragraph, with **no empty line** between paragraph and marginal component.

There are two types of marginal components:

* Pull quotes/key statements
* Marginal modules

There must be at least three hyphens following/preceding the colon.
More hyphens are allowed to increase the readability of the code.

.. HINT::
    **Collapsing marginals:** If the paragraph is less high than the hight of all corresponding marginals, the marginal components collapse and show on hover unless the paragraph is followed by a paragraph without marginal components.


Pull quote
----------

Key statements in the text, so called pull quotes, can be added to the marginals to catch attention and give readers an idea about the adjacent content.

| :syntax:`:--- KEYSTATEMENT ---:`
| :variable:`pull quote`
| :syntax:`:---:`


**Example**

.. code:: md

    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur odio maxime ad itaque earum, aliquam hic neque inventore minima ea doloribus. Voluptatibus illo incidunt, est, consequatur quam quae.
    :----------- KEYSTATEMENT -----------:
    Adipisci consectetur odio maxime ad itaque earum.
    :------------------------------------:


.. _Marginal module:

Marginal module
---------------

.. sidebar:: Smart clusters

   Create your own categorisation of marginals. Define a limited number of modules, pick a comprehensive icon for each and cluster all your additional information according to the chosen categories.

Marginal modules are textblocks preceeded by an icon. Markdown syntax and inline components can be used in marginal modules.

| :syntax:`:---`  :variable:`marginal module slug`  :syntax:`---:`
| :variable:`marginal module content`
| :syntax:`:---:`

The modules receive the CSS class :code:`.ms-aside-SLUG`. The icons are taken from the Material icon font and are defined by the theme.

The default graphite theme currently supports the following modules:

.. code:: scss

    //  Define icons for marginal modules
    //
    //  module slug   :  Material icon slug
    //  -----------      ------------------
    $ms-icons: (
        link          :  earth,
        licence       :  copyright,
        caption       :  information-variant,
        author        :  account,
        twitter       :  twitter,
        linkedin      :  linkedin,
        glossary      :  book-open-variant,
        note          :  star,
        sidenote      :  star,
        download      :  download,
        slidedeck     :  chart-pie,
        reference     :  tooltip-text,
        translate     :  translate,
        generalSource :  format-quote-close,
        institution   :  domain,
        facebook      :  facebook,
        youtube       :  youtube-play,
    );

    // ...

    // Assign icons to classes
    @each $ms-type, $ms-icon in $ms-icons {
        .ms-aside-#{$ms-type} p{ @extend .mdi-#{$ms-icon}; }
    }


**Examples**

.. code:: md

    :--- NOTE ---:
    Lorem ipsum dolor sit amet, **consectetur adipiscing** elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
    :------------:


.. code:: md

    :--- LINK ---:
    [NetzDG ( Art. 2)](https://www.gesetze-im-internet.de/netzdg/BJNR335210017.html)
    :------------:


.. _Inline component:

Inline component
================


.. _Reference:

Reference
----------

The inline reference to a source in the text consists of a slug to the full reference and the text displayed.

:syntax:`[: REFERENCE |` :variable:`reference slug` :syntax:`|` :variable:`reference caption`  :syntax:`\ :]`


**Example**

.. code:: md

    This is text [: REFERENCE | AuthorCoauthor2020 | Author, F., Coauthor, S. 2016 :] that goes on.

Which will link to the item in the reference list :file:`pages/references.yaml` with the according slug.

.. TODO::
    add link to reference list documentation

.. code:: yaml

  AuthorCoauthor2020:
      short: "Author, F., Coauthor, S. (2016). Some fancy title, 7(1)."
      long: "Author, F., Coauthor, S. (2016). Some fancy title, 7(1). 2053951719897945."
      url: "http://someurl.com"

.. TIP::
   To display reference icons only, simply leave the element after the second | blank.


Sidenote
--------

Marginal notes can refer to a particular element in the text by referencing the sidenote within the text.

:syntax:`[: SIDENOTE |` :variable:`term` :syntax:`\ :]`

Followed by the :ref:`Marginal module`:

| :syntax:`:--------- SIDENOTE |` :variable:`term` :syntax:`\ ---------:`
| :variable:`Explanation`
| :syntax:`:---------------------------------------------------------------------------:`

**Example**

.. code:: md

    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur odio maxime ad itaque earum [: SIDENOTE | molestias :], aliquam hic neque inventore minima ea doloribus. Voluptatibus illo incidunt, est, consequatur quam quae.
    :--- SIDENOTE | molestias ---:
    See [Some link](https://#): Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    :------------:

Glossary item
-------------

Glossary items can be added to the text. The explanation will show in the marginal column. Use Markdown formatting to style the glossary entry as desired.

:syntax:`[: GLOSSARY |` :variable:`glossary slug` :syntax:`\ |\ ` :variable:`glossary caption` :syntax:`\ :]`

Followed by the marginal component:

| :syntax:`:--------- GLOSSARY |` :variable:`glossary slug` :syntax:`\ ---------:`
| :variable:`Glossary explanation text with Markdown formatting`
| :syntax:`:---------------------------------------------------------------------------:`

**Example:**

.. code:: md

    Alongside human reviewers called content moderators, platforms use automation and AI to identify and respond to problematic content and behaviour. The benefit of [: GLOSSARY | ACM | algorithmic content moderation (ACM) :] is that it is a fast and globally scalable way to prevent offensive content being uploaded and travelling across the globe within seconds.
    :--- GLOSSARY | ACM ---:
    **ACM**: Platforms use human reviewers, known as _content moderators_, to screen posts and accounts for abuse. Because of the large amount of activity that happens on platforms everyday, content moderation is too large a task for human content moderators alone. Platforms therefore use technical automation to identify and sanction violating posts and accounts. ACM refers to "systems that classify user-generated content based on either matching or prediction, leading to a decision and governance outcome (e.g. removal, geoblocking, account takedown)"[: REFERENCE | GorwaKatzenbach2020 | :]. This could be as simple as a bot that deletes posts with a certain keyword in them. However, large platforms routinely and increasingly use complex, advanced technologies, such as machine learning (ML), to undertake tasks in content moderation.
    :---------------------:

.. HINT::
    Inline components such as a :ref:`reference` can be used in the marginal of inline components.

.. _Container component:

Container component
===================

.. sidebar:: Multi-layer information

   Strengthen your article by adding additional data layers to your  figures or interactive visualisations. Link to underlaying data sets or more extensive tables when showing a data interpretation. The quote component allows you to complement a translated statement with the original quote and offers more information about the quotee.

A container component streches over all columns. The marginal column  contains descriptive information as well as share, full screen and download buttons.

The component must be wraped by empty lines with at least three hyphens following/preceding the colon. More hyphens are allowed to increase the readability of the code. YAML syntax is used within the component.

.. _Figure:

Figure
------

A figure will show as full-column element. Add alternative information to increase accessability if images are not displayed. Description, author and licence information are not mandatory.

.. TODO::
    Mandatory items? Link to data?

| :syntax:`:--- FIGURE ---:`
| :syntax:`file:` :variable:`path to file`
| :syntax:`alt:` :variable:`alt attribute for image`
| :syntax:`caption:` :variable:`title of figure`
| :syntax:`description:` :variable:`description/further information`
| :syntax:`author:` :variable:`author/rights holder`
| :syntax:`licence:` :variable:`copyright licence`
| :syntax:`:---:`


**Example:**

.. code:: yaml

    :------------------------------- FIGURE --------------------------:
    file: images/studienelemente.svg
    author: Impact Distillery
    licence: CC BY SA 3.0
    alt: Die Abbildungs zeigt die Visualisierung der Studienelemente, bestehend aus X, Y und Z.
    caption: Studienelemente
    description: Der Aufbau der Studie im Überblick
    :-----------------------------------------------------------------:

.. seealso::

    For the full-width component refer to :ref:`Full-width figure`.

Video
-----

The video component allows embedding of YouTube videos.

.. TODO::
    Mandatory items? Only Youtube? Only load after click by default implemented?

| :syntax:`:--- FIGURE ---:`
| :syntax:`url:` :variable:`url of YouTube vide in the format https://www.youtube.com/embed/VIDEOID`
| :syntax:`caption:` :variable:`title of video`
| :syntax:`description:` :variable:`description/further information`
| :syntax:`authorDescription:` :variable:`author information`
| :syntax:`linkedinName:` :variable:`LinkedIn profile handle (w/o url)`
| :syntax:`twitterName:` :variable:`Twitter profile handle (w/o url)`
| :syntax:`:---:`

**Example:**

.. code:: yaml

    :------------------------- VIDEO --------------------------:
    url: https://www.youtube.com/embed/-qCtxCHBBhw
    caption: "Gespräch  mit Moritz Kreppel"
    authorDescription: Urban Sports Club
    linkedinName: moritzkreppel
    twitterName: MoritzKreppel
    description: "1. Welche Erfahrungen haben Sie in der Zusammenarbeit mit etablierten Unternehmen gemacht?<br>
    2. Wie verläuft die Identifikation und Ansprache interessanter Unternehmen?<br>
    3. Welche Faktoren haben die Zusammenarbeit positiv beeinflusst?<br>
    4. Warum könnte eine Zusammenarbeit mit etablierten Unternehmen, einer Kooperation mit Großkonzernen vorgezogen werden?"
    :----------------------------------------------------------:


Blockquote
----------

A blockquote shows as full column element. Orginal quotes can be added when translated, author details and social media links are not mandatory.

| :syntax:`:--- QUOTE ---:`
| :syntax:`quote:` :variable:`quote`
| :syntax:`quoteOriginal:` :variable:`quote in original language`
| :syntax:`author:` :variable:`quotee`
| :syntax:`authorDescription:` :variable:`quotee details, affiliation or short bio`
| :syntax:`linkedinName:` :variable:`LinkedIn profile handle (w/o url)`
| :syntax:`twitterName:` :variable:`Twitter profile handle (w/o url)`
| :syntax:`:---:`

**Example:**

.. code:: yaml

    :------------------------- QUOTE --------------------------:
    quote: "Wenn du als Startup nicht kooperierst hast du keine Chance."
    quoteOriginal: "As a small company, you don’t have a chance without collaborating."
    author: "Gilad Amitai"
    authorDescription: "Ubimo"
    linkedinName: giladamitai
    twitterName: gamitai
    :----------------------------------------------------------:


Table
-----

Simple Markdown tables are rendered within the text, more complex tables should be visualised with the table component. Header rows and columns are possible, a download button links to the data file.

| :syntax:`:--- CSV ---:`
| :syntax:`file:` :variable:`path to csv file`
| :syntax:`caption:` :variable:`caption of table`
| :syntax:`description:` :variable:`description/further information`
| :syntax:`header-row:` :variable:`true or false`
| :syntax:`header-column:` :variable:`true or false`
| :syntax:`:---:`

**Example:**

.. code:: yaml

    :-------------- CSV ------------------:
    file: assets/tables/table.csv
    caption: Lorem ipsum dolor sit amet
    description: Amet dictum sit amet justo donec enim et leo duis ut diam
    header-row: true
    header-column: true
    :-------------------------------------:


Author
------

An author component presenting authors, editors or other persona relevant for the publication.

| :syntax:`:--- AUTHOR ---:`
| :syntax:`file:` :variable:`path to csv file`
| :syntax:`name:` :variable:`author name`
| :syntax:`institution:` :variable:`author affiliation or position`
| :syntax:`website:` :variable:`link to company or personal website`
| :syntax:`linkedinName:` :variable:`LinkedIn profile handle (w/o url)`
| :syntax:`twitterName:` :variable:`Twitter profile handle (w/o url)`
| :syntax:`description:` :variable:`Short bio or person details`
| :syntax:`:---:`

.. code:: yaml

    :---------------------- AUTHOR ----------------------:
    file: assets/images/authors/image-of-author.png
    name: Martha Mustermann
    institution: Brand Inc.
    website: https://www.impactdistillery.de/graphite
    linkedinName: sample
    description: Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
    :----------------------------------------------------:


Carousel
--------

Multiple container components can be shown as carousel. Slides are seperated by three hypens, component details need to be indented.

| :syntax:`:--- SLIDES ---:`
| :variable:`container component slug` :syntax:`:`
|   :variable:`... container component yaml content`
| :syntax:`---`
| :variable:`container component slug` :syntax:`:`
|   :variable:`... container component yaml content`
| :syntax:`:---:`

**Example:**

.. code:: yaml

    :------------------------- SLIDES --------------------------:
    quote:
        quote: "Der Mittelstand ist unglaublich spannend. Viele schauen immer auf die DAX-Konzerne, aber der Mittelstand bietet unglaublich viel Potenzial für Startups und er öffnet sich ihnen gegenüber mehr und mehr. Es gibt ein paar erste treibende Kräfte und die Tendenz, dass viele mittelständische Unternehmen mittlerweile die Wichtigkeit des Themas erkannt haben. Darüber hinaus ist das Thema Digitalisierung nicht mehr nur ein Gespenst, sondern Realität."
        author: "Roman Neumann"
        authorDescription: "VR Leasing AG"
        linkedinName: roman-neumann-b2a13a33
    ---
    quote:
        quote: "In 2017 sehen wir immer häufiger, dass sich viele Leute immer besser mit Startups auskennen und es mittlerweile eine gemeinsame Sprache gibt. Die Erfahrungen und das Wissen, wie man mit Startups kommuniziert und umgeht, nehmen kontinuierlich zu."
        quoteOriginal: "I think in 2017 we’re starting to see that people are much more familiar with startups and that there’s common language. There’s tribal knowledge in knowing how to talk or deal with the startups."
        author: "Angelia Müller"
        authorDescription: "Techstars"
        linkedinName: angiemuller
        twitterName: mullermilk
    ---
    quote:
        quote: "Wenn du als Startup nicht kooperierst hast du keine Chance."
        quoteOriginal: "As a small company, you don’t have a chance without collaborating."
        author: "Gilad Amitai"
        authorDescription: "Ubimo"
        linkedinName: giladamitai
        twitterName: gamitai
    :----------------------------------------------------------:

.. _Full-width component:

Full-width component
====================

Full with components span the full with of the page.

Chapter header
--------------

Full width chapter headers with headline, subheadline and background image.

| :syntax:`:--- CHAPTER_HEADER ---:`
| :syntax:`image:` :variable:`url to background image`
| :syntax:`authors:` :variable:`chapter authors`
| :syntax:`title:` :variable:`chapter headline`
| :syntax:`subtitle:` :variable:`chapter subheadline`
| :syntax:`thumbnail:` :variable:`url to graphic/icon left of content`
| :syntax:`:---:`

**Example:**

.. code:: yaml

    :-------------------- CHAPTER_HEADER --------------------:
    image: "path/to/background-image.jpg"
    authors: "Joan London & Jack Middleton"
    thumbnail: "path/to/trailing-icon.png"
    title: Introduction
    subtitle: Bibendum ut tristique et egestas quis ipsum suspendisse ultrices
    :---------------------------------------------------------:


Infobox
-------

Collapsable section for case studies, excursus or similar.

| :syntax:`:--- INFOBOX ---:`
| :syntax:`title:` :variable:`title of infobox`
| :syntax:`description:` :variable:`description of infobox`
| :syntax:`note:` :variable:`key learnings or quick summary`
| :syntax:`link:` :variable:`list of links`
| :syntax:`file_url:` :variable:`url to download`
| :syntax:`file_label:` :variable:`label of download`
| :syntax:`collapse:` :variable:`true/false, defaults to false`
| :syntax:`---`
| :variable:`infobox component content (md)`
| :syntax:`:---:`

**Example:**

.. code:: yaml

    :---------------------- INFOBOX ---------------------------:
    title: Lorem ipsum dolor sit amet
    description: Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
    note: "<strong>Key-Learnings:</strong><br>
    Duis aute irure dolor in reprehen derit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.<br>
    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    link:
    - http://www.loopline-systems.com
    - http://www.allfoye.net
    ---
    ## Headline for the excursus
    Augue mauris augue neque gravida in fermentum et sollicitudin ac. Scelerisque fermentum dui faucibus in ornare quam. Malesuada fames ac turpis egestas sed. Nisi porta lorem mollis aliquam ut porttitor. Tortor dignissim convallis aenean et tortor at risus viverra. Purus sit amet luctus venenatis lectus magna fringilla. Nulla at volutpat diam ut venenatis tellus in metus.

    Amet commodo nulla [: REFERENCE | Lorem2020 | facilisi :] nullam vehicula. Id velit ut tortor pretium viverra suspendisse potenti. Sed nisi lacus sed viverra. Mi quis hendrerit dolor magna eget est. A diam sollicitudin tempor id eu. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. At erat pellentesque adipiscing commodo elit at imperdiet.
    :----------------------------------------------------------:

.. _Full-width figure:

Full-width figure
-----------------

Component to display figures spaning the full width of the page.

.. TODO::
    Mandatory items? Link to data? Do all fields work?

| :syntax:`:--- FULL_FIGURE ---:`
| :syntax:`file:` :variable:`path to file`
| :syntax:`alt:` :variable:`alt attribute for image`
| :syntax:`caption:` :variable:`title of figure`
| :syntax:`description:` :variable:`description/further information`
| :syntax:`author:` :variable:`author/rights holder`
| :syntax:`licence:` :variable:`copyright licence`
| :syntax:`:---:`


**Example:**

.. code:: yaml

    :------------ FULL_FIGURE ------------:
    file: assets/images/figures/some-figure-de.svg
    alt: Figure visualising something.
    caption: Duis aute irure dolor in reprehen   derit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
    :-------------------------------------:

.. seealso::

    For standard figures see container component :ref:`figure`.


Additional plugins
==================

.. _List of references:

List of references
------------------

Prints the list of references defined in :file:`pages/references.yaml`.

| :syntax:`:--- LISTOFREFERENCES ---:`
| :syntax:`title:` :variable:`Title above list`
| :syntax:`:---:`


.. HINT::
    **Does your page throw errors instead of displaying the reference list?** 

    The devil is in the details. Make sure your `references.yaml` doesn't contain any syntax errors. Use typographical quotes within your citations and prevent the use of special characters for reference slugs.


List of figures
---------------

Prints a list of figures.

| :syntax:`:--- LISTOFFIGURES ---:`
| :syntax:`title:` :variable:`Title above list`
| :syntax:`:---:`

.. TODO::
    Plugins to test and document

    * TML Plugin
    * efault Plugin
    * AML Plugin
    * SON Plugin
    * amlMd Plugin
    * ariable Plugin

HTML Plugin
-----------

Default Plugin
--------------

YAML Plugin
-----------

JSON Plugin
-----------

YamlMd Plugin
-------------

Variable Plugin
---------------
