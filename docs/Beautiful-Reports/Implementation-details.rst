=======================
 Implementation details
=======================

Page strucuture
---------------

::

    body
        .page-wrap
            nav
            header
            .jumbotron
                p.author
                h1
            article
                .abstract
                .article-info
                section.h2-section
                    h2
                    ...
                    section.h3-section
                        h3
                        ...
                    section.h3-section
                        h3
                        ...
                section.h2-section
                    h2
                    section.h3-section
                    section.h3-section
                .contributions.references


\_\_\_\_ ROW : figure :: caption: """ : url::""

----/ROW

\_\_\_\_ ROW : text

MD

----/ROW

File structure
--------------

::


    main.py

    config.yaml (theme, technisch)
    module-registration.yaml
    tabs.yaml
    meta.yaml
    audiences.yaml

    THEMES
        CORE
            STYLES
                computed-style.css
                SCSS
                    theme.scss (lädt partials)
                    _variables.scss
                    _colors.scss
                    _layout.scss
                    _grid.scss
                    _mixins.scss
                    MODULES
                        _video.scss
                        _quote.scss
                        _video-youtube.scss
            SCRIPTS
                main.js
                MODULES
                    video.js
            TEMPLATES
                header.html
                .....
                footer.html
        MSTATS
            STYLES
                computed-style.css
                SCSS
                    _variables.scss (change look)
                    _colors.scss
                    MODULES
                        _video-youtube.scss
            SCRIPTS
            TEMPLATES
                footer.html (Piwik)
    CONTENT
        main.md
        PARTIALS
            intro.md
            methods.md
            results.md
            abstract.md
            executive-summary.md
        VIDEOS
            adam.yaml
            eva.yaml
        QUOTES
            all-english-quotes.yaml


