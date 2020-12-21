.. role:: variable
    :class: guilabel variable

.. role:: syntax
    :class: guilabel syntax

**********
Components
**********


Inline components
=================


References
----------

The inline reference to a source in the text consists of a slug to the full reference and the text displayed.

:syntax:`[: REFERENCE |` :variable:`reference slug` :syntax:`|` :variable:`reference caption`  :syntax:`\ :]`


**Example**

.. code:: md

    This is text [: REFERENCE | AuthorCoauthor2020 | Author, F., Coauthor, S. 2016 :] that goes on.

Which will link to the item in the reference list :file:`pages/references.yaml` with the according slug.

.. code:: yaml

  AuthorCoauthor2020:
      short: "Author, F., Coauthor, S. (2016). Some fancy title, 7(1)."
      long: "Author, F., Coauthor, S. (2016). Some fancy title, 7(1). 2053951719897945."
      url: "http://someurl.com"

.. TIP::
   To display reference icons without inline citation just leave the last element blank.


Sidenote
--------

Marginal notes can refer to a particular element in the text by referencing the sidenote within the text.

:syntax:`[: SIDENOTE |` :variable:`term` :syntax:`\ :]`

Followed by the marginal element:

| :syntax:`:--------- SIDENOTE |` :variable:`term` :syntax:`\ ---------:`
| :variable:`Explanation`
| :syntax:`:---------------------------------------------------------------------------:`

**Example**

.. code:: md

    Lorem ipsum dolor sit amet, consectetur adipisicing elit. Adipisci consectetur odio maxime ad itaque earum [: SIDENOTE | molestias :], aliquam hic neque inventore minima ea doloribus. Voluptatibus illo incidunt, est, consequatur quam quae.
    :--- SIDENOTE | molestias ---:
    See [Some link](https://#): Lorem ipsum dolor sit amet, consectetur adipisicing elit.
    :------------:

Glossary
--------

.. code:: md

    Alongside human reviewers called "content moderators", platforms use automation and AI to identify and respond to problematic content and behaviour. The benefit of [: GLOSSARY | ACM | algorithmic content moderation (ACM) :] is that it is a fast and globally scalable way to prevent offensive content being uploaded and travelling across the globe within seconds. It can also spare human content moderators some of the tedium of a very repetitive job, as well as the trauma of viewing the most distressing content, such as child abuse imagery.
    :--- GLOSSARY | ACM ---:
    **What is ACM?**
    Platforms use human reviewers, known as content moderators, to screen posts and accounts for abuse. Because of the large amount of activity that happens on platforms everyday, content moderation is too large a task for human content moderators alone. Platforms therefore use technical automation to identify and sanction violating posts and accounts. ACM refers to "systems that classify user-generated content based on either matching or prediction, leading to a decision and governance outcome (e.g. removal, geoblocking, account takedown)"[: REFERENCE | GorwaKatzenbach2020 | :]. This could be as simple as a bot that deletes posts with a certain keyword in them. However, large platforms routinely and increasingly use complex, advanced technologies, such as machine learning (ML), to undertake tasks in content moderation.
    :---------------------:

Marginal components
===================

Pull quotes
-----------

.. code:: md

    :--- KEYSTATEMENT ---:
    A dearth of information is not an acceptable status quo, when citizens would be best served understanding the way a platform works in order to make informed decisions on whether and how to engage online
    :--------------------:


Marginal note/module
--------------------

.. code:: md

    :--- NOTE ---:
    IEEE Standard 1028-2008 (defining audits as conducted by third parties)
    :------------:


.. code:: md

    :--- LINK ---:
    [NetzDG ( Art. 2)](https://www.gesetze-im-internet.de/netzdg/BJNR335210017.html)
    :------------:

-----------

Container components
=====================

Figure
------

::

    :------------------------------- FIGURE --------------------------:
    file: images/SUM_studienelemente.svg
    author: Alexander von Humboldt Institut für Internet und Gesellschaft
    licence: CC BY SA 3.0
    alt: Die Abbildungs zeigt die Visualisierung der Studienelemente. Diese bestehen aus drei World Cafes mit Gruppendiskussionen beim Tech Open Air, einem Roundtable Meeting mit ExpertInnen am HIIG, vier Workshops zu den Kollaborationsphasen Learn, Match und Partner im Digital Spielfeld Hub, einer schriftlichen Befragung und 20 Interviews mit ExpertInnen aus den USA und Deutschland.
    caption: Studienelemente
    description: Der Aufbau der Studie im Überblick
    :-----------------------------------------------------------------:


Video
-----

::

    :------------------------- VIDEO --------------------------:
    url: https://www.youtube.com/embed/-qCtxCHBBhw
    caption: "Gespräch  mit Moritz Kreppel"
    authorDescription: Urban Sports Club
    linkedinName: moritzkreppel
    twitterName: MoritzKreppel
    description: "1. Welche Erfahrungen haben Sie in der Zusammenarbeit mit etablierten Unternehmen gemacht?<br>
    2. Wie verläuft die Identifikation und Ansprache interessanter Unternehmen?<br>
    3. Welche Faktoren haben die Zusammenarbeit positiv beeinflusst?<br>
    4. Warum könnte eine Zusammenarbeit mit etablierten Unternehmen, einer Kooperation mit Großkonzernen vorgezogen werden?
    "
    :----------------------------------------------------------:

Slider
------

::

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



Full-width components
=====================

Infobox
-------

::

    :---------------------- INFOBOX ---------------------------:
    title: Lorem ipsum dolor sit amet
    description: Vertriebspartnerschaft zwischen Loopline Systems und Allfoye
    note: "<strong>Key-Learnings:</strong><br>
    Eine Ansprechperson, der die Kooperation aktiv vorantreibt und über Entscheidungskompetenzen verfügt, ist ein Kennzeichen für Commitment.<br>
    Die persönliche Beziehung ist für den Erfolg der Partnerschaft entscheidend.<br>
    Wenn es eine kooperative Denkweise im Unternehmen gibt, ist es einfacher, von vornherein interne Schwierigkeiten aus dem Weg zu räumen."
    link:
    - http://www.loopline-systems.com
    - http://www.allfoye.net
    ---
    ## Fallbeispiel: Vertriebspartnerschaft zwischen Loopline Systems und Allfoye
    Loopline Systems ist ein Software-as-a-Service-Startup, das IT-Lösungen im Bereich HR für bessere Feedbackprozesse in Unternehmen anbietet. Allfoye ist eine mittelständische Unternehmensberatung, die Beratungsleistungen zu neuen Geschäftsmodellen und digitaler Transformation bereitstellt. Die beiden Unternehmen arbeiten in einer Vertriebspartnerschaft zusammen, wobei Allfoye die Loopline Systems Software wiederum seinen Kunden zur Verfügung stellt.

    In der anschließenden Match-Phase konnte Allfoye Loopline Systems zu verschiedenen Aspekten beraten, dabei unter anderem bei der Preisgestaltung. Aus Startup-Sicht fand es Nora Heer weiterhin wichtig, schon bereits zu Beginn bestimmte Abmachungen vertraglich festzuhalten. Es folgten noch einige Meetings und gegenseitige Besuche und nach zwei Wochen konnte der Vertrag schließlich unterschrieben werden. Für die Partner-Phase ist eine regelmäßige Überprüfung der gemeinsam definierten Ziele geplant.
    :----------------------------------------------------------:

Full-width figure
-----------------

Chapter header
--------------

.. code:: yaml

    :-------------------- CHAPTER_HEADER --------------------:
    image: "assets/images/pineapple-supply-co-Q7PclNhVRI0-unsplash.jpg"
    title: Introduction
    subtitle: Audits should be mandated by law within the four principles of independence, access, publicity, and expertise
    :---------------------------------------------------------:


:--- CSV ---:
file: assets/tables/appendix-a.csv
caption: Laws and Bills with legal provisions on content moderation by social media platforms
description: "_Law/Bill_: national laws introduced in the last 4 years and bills currently under discussion that introduce regulation on content moderation by social media platforms. \n\n
There are some cases where the content addressed by the law is not clear, particularly  in relation to fake news.
\n\n
_Transparency measures_ in the use of AI and algorithms for content moderation, not for other purposes. Some laws or bills include among the information to be provided by platforms, for example, methods or methodology employed in the detection of irregularity”, which could include information on algorithms and AI, but it is not clear about that.  "
header-row: true
header-column: true
:-----------:
