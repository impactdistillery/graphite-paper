Getting started
===============

Do you want to create a website from a single source or do you want to create your own theme and build up a publication series?


Install graphite-paper
----------------------

Mac OS
^^^^^^

xCode command line tools

.. code:: shell

    # Check if exist:
    $ xcode-select --version

    # Otherwise install:
    $ xcode-select --install

Homebrew

.. code:: shell

    # Check if exist:
    $ brew --version

    # Otherwise install:
    $ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

Python (^3.7)

.. code:: shell

    # Check for installed version:
    $ brew info python

    # Otherwise install:
    $ brew install python@3.7


Pipenv

.. code:: shell

    # Check if exists:
    $ pipenv --version

    # If none installed, check which pip is installed
    $ pip --version
    $ pip3 --version

    # Install pipenv, use pip or pip3 depending on which routes to python 3.x
    $ sudo pip3 install pipenv

Clone repository

.. code:: shell

    # Move to folder, where the article files shall be located (use tab key to autocomplete)
    $ cd ~/PATH_TO_FOLDER_FROM_HOME_DIRECTORY

    # Copy repository url from github and clone
    $ git clone REPOSITORY_URL


Setup Adobe Brackets as graphite environment
--------------------------------------------

You can use the text editor of your choice to create a graphite paper. If you're not too familiar with the command line, we recommend the use  of `Brackets <https://brackets.io>`_ on Mac, a free and easy to use editor that comes with a graphical git extension.

Install brackets from `brackets.io <https://brackets.io>`_ or:

::

    $ brew cask install brackets

Add Extensions to Brackets (File › Extension Manager):

* `Brackets Git <https://github.com/brackets-userland/brackets-git>`_ by  Martin Zagora
* `Markdown Toolbar <https://github.com/alanhohn/markdown-toolbar>`_ Alan Hohn

Start development environment
-----------------------------

Change into repository folder.

If you're there for the first time, do an install

.. code:: shell

    $ pipenv install

Then start environment

.. code:: shell

    $ pipenv shell

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
    Currently the static folder needs to be located in the root folder. It needs to be copied manually into the root folder of the server in order for the paper to work within a subdirectory.
