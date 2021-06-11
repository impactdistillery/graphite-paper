**Sample meta.yaml:**

.. code:: yaml

    # PUBLICATION META INFO
    # —————————————————————

    title:                  "Das Scholar-led.network-Manifest"
    subtitle:               "Wissenschaftliche Publikationen im Open Access, von der
    wissenschaftlichen Community betrieben, gefördert, geleitet"
    authors:                ""
    year:                   2021
    date_publication:       Mai 2021
    # date_submission:
    # date_last_updated:

    # keywords:
    abstract:               "Das Manifest ist das Ergebnis der Diskussionen in der Fokusgruppe Scholar-led.network (als Teil des open-access.networks). Es beschreibt die Zusammensetzung einer Gruppe von Scholar-led Akteur*innen in Deutschland, umreißt deren zentrale Kritik am gegenwärtigen, wissenschaftlichen Publikationssystem und definiert Handlungsfelder für faires, planvolles und vielfältiges Publizieren."

    cite_as:               "Fokusgruppe Scholar-led.network. (2021) *Das Scholar-led.network-Manifest*. DOI: XXX"

    pdf_url:                https://doi.org/10.5281/zenodo.4291999
    doi:                    10.5281/zenodo.4291999
    # isbn:                   978-989-746-128-6
    contact_email:          marcel.wrzesinski@hiig.de

    short_url:              https://graphite.page/hiig-dapla
    social_image_url:       https://graphite.page/hiig-dapla/assets/images/social.png
    lang:                   de


    # PUBLICATION STYLE
    # —————————————————————
    styles:                 theme/styles/manifesto.css
    background_url:         assets/images/amanda-lins-aVKUVLIsl1o-unsplash.jpg



    # DISCLAIMER
    # —————————————————————
    data_usage:
    disclaimer:
    terms_of_use:
    licence:

    # Author info is shown in footer bar and on the right, if no logo is provided.
    author_info:            Ein Manifest der Fokusgruppe Scholar-led im Rahmen des Projekts open-access.network
    logo_url:


    # SETTINGS
    # —————————————————————

    author_info_sticky:     true
    no_journal:             true
    matomo_tracking:        true
    matomo_url:             "https://piwik.wunderjewel.de/"
    matomo_siteId:          "4"


    # PUBLISHER INFO
    # thanks for mentioning graphite
    # —————————————————————

    brand:                  graphite – Enhanced publications for a digital environment
    brand_url:              https://www.impactdistillery.com/graphite
    brand_logo:             theme/images/graphite.svg

    # Infos in expandable header
    # imprint:                "Dieses Manifest ist als Ergebnis der Diskussionen in der [Fokusgruppe Scholar-led](https://open-access.net/digitale-fokusgruppen/fokusgruppe-scholar-led) im Rahmen des Projekts [open-access.network](https://open-access.net/digitale-fokusgruppen) entstanden.\n\n
    # Die Veröffentlichung wurde mit Graphite erstellt, ein Open-Source-Framework für digitales Publizieren."

    # further_publications:
    #   - label: Kooperationen zwischen Startups und Mittelstand
    #     url: https://www.impactdistillery.com/graphite/hiig-sum/
    #   - label:  Plattforminnovation im Mittelstand
    #     url: https://graphite.page/hiig-dapla/

    # further_links:
    #   - label: Graphite Projektwebsite
    #     url: https://www.impactdistillery.com/graphite
    #   - label: graphite-paper auf PyPI
    #     url: https://pypi.org/project/graphite-paper


    :---------------------------------------------------:
    # TABS
    # —————————————————————

    tabs:
      - title: "Manifest"
        slug: index
        include_abstract: true
        md_container: article
      - title: "Autor*innen"
        slug: editors
        md_container: section
      - title: "Referenzen"
        slug: directories
        md_container: section
      - title: "Zur Fokusgruppe"
        slug: about
        md_container: section


Available meta fiels
---------------------


======================  ==========================================  ====================
Key                     Value                                       Comment
======================  ==========================================  ====================
**PUBLICATION META INFO**
----------------------------------------------------------------------------------------
title                   Publication title                           **mandatory**
subtitle                Publication subtitle
authors                 Last Name, F. N., Last Name, F. N., & Last  | **mandatory**
                        Name, F. N.                                 | (use ""
                                                                      if no authors)
year                    Year of publication
date_publication        Date of publication
date_submission         Date of submission
date_last_updated       Date of most recent update
keywords                Keywords (comma separated)
abstract                Abstract                                    | md syntax and
                                                                      inline
                                                                    | components
                                                                      supported
cite_as                 Citation suggestion                         md syntax supported
pdf_url                 Url to pdf file
doi                     Digital Object Identifier
isbn                    ISBN
contact_email           Email address of contact person
short_url               Final publication URL
social_image_url        **Absolute** path to share pic              Used for sharing
lang                    2-digit language code (de/en)
**PUBLICATION STYLE**
----------------------------------------------------------------------------------------
styles                  theme/styles/STYLESHEET_NAME.css
background_url          assets/images/HEADER_IMAGE.jpg
**DISCLAIMER**
----------------------------------------------------------------------------------------
data_usage:             How can and shall research data be used?
disclaimer:             Need to add a disclaimer?
terms_of_use:           Add terms of use here
licence:                Add licence here                            e.g., CC-BY-4.0
author_info             Shown in footer and instead of logo
                        if none provided
logo_url                Relative path to publisher logo
**SETTINGS**
----------------------------------------------------------------------------------------
author_info_sticky      Make footer bar sticky                      true/false
no_journal              Disable expandable top navigation           true/false
matomo_tracking         Enable Matomo statistics                    true/false
matomo_url              URL of Mataomo tracking
matomo_siteId           Matomo site ID
**PUBLISHER INFO**
----------------------------------------------------------------------------------------
brand                   graphite or whitelabel brand
brand_url               URL to graphite or whitelabel brand
brand_logo              Relative path to brand logo
imprint                 Left column of top navigation               md syntax supported
further_publications    List of further journal publications        yaml list syntax
further_links           Link list with external content             yaml list syntax
**Tabs**
----------------------------------------------------------------------------------------
tabs                    List of tabs for publication (see below)    yaml list syntax
======================  ==========================================  ====================


Define tabs:

======================  ==========================================
Tabs subkey             Value
======================  ==========================================
title                   Tab caption
slug                    Tab slug for URL
include_abstract        Include abstract and meta infos on top
md_container            | HTML tag wrapping tab content
                        | Sample theme provides styles
                          for :code:`article` and
                          :code:`section`
======================  ==========================================



