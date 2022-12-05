Getting started
===============

Do you want to create a website from a single source or do you want to create your own theme and build up a publication series?


Install requirements
--------------------

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

Python (^3.8)

.. code:: shell

    # Check for installed version:
    $ brew info python

    # Otherwise install:
    $ brew install python@3.8


Pipenv

.. code:: shell

    # Check if exists:
    $ pipenv --version

    # If none installed, check which pip is installed:
    $ pip --version
    $ pip3 --version

    # Install pipenv, use pip or pip3 depending on which routes to python 3.x:
    $ sudo pip3 install pipenv


Windows
^^^^^^^

Install from official websites:

    - Python (Make sure to check the box for PATH variables to be set)
    - Git (includes Git-Bash)

Open Git-Bash to install Pipenv 

.. code:: shell

    # Check if exists:
    $ pipenv --version

    # Install pipenv:
    $ pip install pipenv

Optional: Pyenv

You might run into errors regarding your installed/default version of python in the further installation steps.

.. code:: shell

    # Install pyenv-win by running the following installation command in a PowerShell terminal:
    $ Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"

    # If you are getting any UnauthorizedAccess error, start Windows PowerShell with the "Run as administrator" option and run 
    Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope LocalMachine
    # now re-run the above installation command

Here you can find detailed installation instructions (via the PowerShell):

 | `https://github.com/pyenv-win <https://github.com/pyenv-win/pyenv-win/blob/master/docs/installation.md#powershell>`_.

Install graphite-paper
----------------------

You can a) work on an existing graphite publication repository, or b) start from scratch with our graphite starter.

Clone existing repository
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: shell

    # Move to folder, where the article files shall be located (use tab key to autocomplete)
    $ cd ~/PATH_TO_FOLDER_FROM_HOME_DIRECTORY

    # Copy repository url from github and clone
    $ git clone REPOSITORY_URL

    # If you're using git for the first time, proceed with promted sign-in procedures

.. _Starter:

Use graphite starter
^^^^^^^^^^^^^^^^^^^^^^^

Our starter is provided by `cookiecutter <https://github.com/cookiecutter/cookiecutter>`_.

.. code:: shell

    # Check for installed version:
    $ cookiecutter --version

    # Otherwise install (OSX/Linux):
    $ brew install cookiecutter

Install the starter.

.. code:: shell

    # Download and init graphite starter:
    $ cookiecutter gh:impactdistillery/graphite-starter

Cookiecutter will prompt you to enter a title, authors etc. for your publication. Your :code:`journal_slug` will be the name of the directory created by cookiecutter.

.. code:: shell

    # Change to your repository
    $ cd JOURNAL_SLUG

Start development environment
-----------------------------

Change into repository folder.

If you're there for the first time, do an install

.. code:: shell

    $ pipenv install

.. WARNING::
    You might run into errors regarding your installed/default version of python.
    Use Pyenv to administer Phython versions in Pipenv. 


Then start environment

.. code:: shell

    $ pipenv shell

.. code:: shell

    $ python PAPER_FOLDER/manage.py runserver

.. TIP::
    The default port is 8000. If you want to run more than one paper at once, you can specify different ports with a blank after :code:`runserver` such as :code:`$ python OTHER_PAPER_FOLDER/manage.py runserver 8001`


Install a text editor to edit your *graphite* publication
---------------------------------------------------------

You can use the text or source code editor of your choice to create a graphite paper. 
If you're not too familiar with the command line, we suggest the use of one of the following editors:

    - `VS Codium <https://vscodium.com>`_, the popular open-source version of VS code with a graphical git interface and an extensive extension library
    - `Brackets <https://brackets.io>`_, a free and easy to use editor for Mac that comes with a graphical git extension
    - Atom `atom.io <https://atom.io>`_

Publish graphite paper
----------------------

Change into repository folder.

.. code:: shell

    $ python PAPER_FOLDER/manage.py build

The paper and all assets will be rendered into the folder :file:`_build`. The contents of this folder can be copied to the desired location or server in order to publish the website.

.. WARNING::
    Currently the static folder needs to be located in the root folder. It needs to be copied manually into the root folder of the server in order for the paper to work within a subdirectory.
