Getting started
===============

Do you want to create a website from a single source or do you want to create your own theme and build up a publication series?


Install graphite-paper
----------------------

**Mac OS**

xCode command line tools
Homebrew

.. code:: shell

    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

Install Python 3

.. code:: shell

    $ brew install python


Install pipenv

Check which pip is installed (`pip --version` or `pip3 --version` and use pip or pip3 depending on which routes to python3)

.. code:: shell

    $ sudo pip install pipenv

Clone repository

.. code:: shell

    $ git clone REPOSITORY_URL

Change into repository folder.


Setup Adobe Brackets as graphite environment
--------------------------------------------

You can use the text editor of your choice to create a graphite paper. If you're not too familiar with the command line, we recommend the use  of Adobe Brackets for Mac, a free and easy to use editor that comes with a graphical git extension.

Install brackets

::

    $ brew cask install brackets

Add Extensions to Brackets (File > Extension Manager):

* `Brackets Git <https://github.com/brackets-userland/brackets-git>`_ by  Martin Zagora
* `Markdown Toolbar <https://github.com/alanhohn/markdown-toolbar>`_ Alan Hohn

Start development environment
-----------------------------

Change into repository folder.

.. code:: shell

    $ python PAPER_FOLDER/manage.py runserver

.. TIP::
    The default port is 8000. If you want to run more than one paper at once, you can specify different ports with a blank after :code:`runserver` such as :code:`$ python OTHER_PAPER_FOLDER/manage.py runserver 8001`

Publish graphite paper
--------------------

Change into repository folder.

.. code:: shell

    $ python PAPER_FOLDER/manage.py build

The paper and all assets will be rendered into the folder :file:`_build`. The contents of this folder can be copied to the desired location or server in order to publish the website.

.. WARNING::
    Currently the static folder needs to be located at the root. It needs to be copied manually into the root folder of the server  in order for the paper to work within a subdirectory.
