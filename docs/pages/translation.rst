.. _translation:

*********************
Translation Support
*********************

Graphite Paper provides comprehensive translation support, allowing you to customize all user-facing text in your publications. This is useful for creating publications in different languages or customizing the terminology to match your publication's style.

How Translation Works
=====================

All user-facing text strings in Graphite Paper can be customized through a ``lang.yaml`` file in your publication's ``config/`` directory. The framework loads this file at build time and uses the values you provide. If a translation key is missing, the framework falls back to English defaults.


Setting Up Translations
========================

1. **Create lang.yaml**

   In your publication's ``config/`` directory, create a file named ``lang.yaml``:

   .. code:: shell

       YOUR_PAPER_SLUG/
       └── config/
           ├── meta.yaml
           └── lang.yaml    # Create this file

2. **Add Translation Keys**

   Add the text strings you want to customize. You only need to include the keys you want to change:

   .. code:: yaml

       # Example: German translations
       abstract: "Zusammenfassung"
       keywords: "Schlüsselwörter"
       download: "Herunterladen"
       powered_by: "Erstellt mit"

3. **Build Your Publication**

   Run the build command as usual. Your custom translations will be used automatically:

   .. code:: shell

       $ python manage.py build


Available Translation Keys
===========================

Navigation and Headers
----------------------

.. code:: yaml

    header_articles: "Further publications"
    header_more: "More information"
    powered_by: "Powered by"
    toc: "Table of content"
    toc_long: "Table of content"

Abstract and Metadata
---------------------

.. code:: yaml

    abstract: "Abstract"
    keywords: "Keywords"
    cite_as: "Cite as"
    licence: "Licence"
    disclaimer: "Disclaimer"
    terms_of_use: "Terms of use"
    questions: "Questions?"
    write_mail: "Write an email to"

Dates
-----

.. code:: yaml

    date_publication: "Published"
    date_submission: "Submitted"
    date_last_updated: "Last updated"

Actions
-------

.. code:: yaml

    download: "Download"
    download_csv: "Download .csv"
    downloadData: "Download the data"
    download_file: "Download file"
    read_on: "Continue reading full article"
    visit_website: "Visit website"

Share Buttons
-------------

.. code:: yaml

    share: "SHARE"

Quote Component
---------------

.. code:: yaml

    quote_open: """      # Opening quotation mark
    quote_close: """     # Closing quotation mark
    translation: "Translation"
    original_version: "Original version"

Infobox Component
-----------------

.. code:: yaml

    expand_infobox: "Expand infobox"
    collapse_infobox: "Collapse infobox"

Default Navigation Content
---------------------------

These keys customize the default content shown in the expandable top navigation when no custom content is provided in ``meta.yaml``:

.. code:: yaml

    default_imprint: "This publication was built with the framework Graphite..."
    default_publication_1_label: "Agility. A whitepaper by LRN LAB"
    default_publication_1_url: "https://www.impactdistillery.com/graphite/..."
    # ... additional defaults available in lang.yaml.example


Complete Example Files
======================

English Publication
-------------------

For an English publication, you typically don't need a ``lang.yaml`` file since English is the default. However, you can create one to customize specific terms:

.. code:: yaml

    # config/lang.yaml - Minimal English customization
    powered_by: "Built with"
    share: "Share"

German Publication
------------------

.. code:: yaml

    # config/lang.yaml - German translation
    
    # Navigation
    header_articles: "Weitere Publikationen"
    header_more: "Mehr Informationen"
    powered_by: "Erstellt mit"
    toc: "Inhaltsverzeichnis"
    
    # Metadata
    abstract: "Zusammenfassung"
    keywords: "Schlüsselwörter"
    cite_as: "Zitieren als"
    licence: "Lizenz"
    
    # Actions
    download: "Herunterladen"
    read_on: "Weiterlesen"
    visit_website: "Website besuchen"
    
    # Share
    share: "TEILEN"
    
    # Quote
    translation: "Übersetzung"
    original_version: "Originalversion"
    
    # Infobox
    expand_infobox: "Infobox erweitern"
    collapse_infobox: "Infobox einklappen"

French Publication
------------------

.. code:: yaml

    # config/lang.yaml - French translation
    
    # Navigation
    header_articles: "Autres publications"
    header_more: "Plus d'informations"
    powered_by: "Propulsé par"
    
    # Metadata
    abstract: "Résumé"
    keywords: "Mots-clés"
    download: "Télécharger"
    
    # Quote
    translation: "Traduction"
    original_version: "Version originale"


Reference File
==============

A complete reference file with all available translation keys is included in the Graphite Paper framework:

.. code:: shell

    graphite_paper/local_django/lang.yaml.example

You can copy this file to your publication's ``config/`` directory and customize it:

.. code:: shell

    $ cp path/to/graphite_paper/local_django/lang.yaml.example YOUR_PAPER_SLUG/config/lang.yaml


Backward Compatibility
======================

Translation support is fully backward compatible:

* **No lang.yaml file**: All text uses English defaults
* **Partial lang.yaml file**: Only specified keys are customized, others use English defaults
* **Invalid keys**: Ignored silently, framework uses English defaults

Existing publications will continue to work without any changes.


Best Practices
==============

1. **Start with Essentials**: Begin by translating the most visible text (abstract, keywords, download buttons)

2. **Use Consistent Style**: Maintain consistent capitalization and punctuation across all translations

3. **Test Your Translations**: Build and preview your publication to ensure all translations appear correctly

4. **Keep a Reference**: Maintain a copy of ``lang.yaml.example`` for reference when adding new translations

5. **Version Control**: Commit your ``lang.yaml`` file to version control along with your publication content


Troubleshooting
===============

**Translations Not Appearing**

* Check that ``lang.yaml`` is in the ``config/`` directory
* Verify YAML syntax (use a YAML validator if needed)
* Ensure key names match exactly (they are case-sensitive)
* Clear your browser cache and rebuild: ``python manage.py build``

**Special Characters Not Displaying**

* Ensure your ``lang.yaml`` file is saved with UTF-8 encoding
* Use YAML string escaping for special characters if needed

**Missing Translations**

* If a key is not in your ``lang.yaml`` file, the English default will be used
* This is intentional - you only need to include keys you want to customize
