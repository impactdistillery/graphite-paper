# Initiate and install

- make new Respository on github online
- clone repository
- copy sample-paper-en und Ppipfile from sample-journal into new repository

$ pipenv install


# Start pipenv (in journal repo)

$ pipenv shell


# Start paper

$ python3 subfolder-paper/manage.py runserver


# Leave virtual environment

Control + D


# Render docs

– Start pipenv of another journal (e.g., GDHRNet)
– go back to graphite-paper

Continuous deployment for docs:

$ sphinx-autobuild docs docs/_build/html

Build docs

$ cd docs
$ make html
