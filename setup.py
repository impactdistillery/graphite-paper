from setuptools import setup

with open("readme.md", "r") as fh:
        long_description = fh.read()

setup(
    name='graphite_paper',
    version='0.0.2',
    description='Graphite Paper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://www.impactdistillery.com/graphite',
    author='Larissa Wunderlich and Marcel Hebing',
    author_email='info@impactdistillery.com',
    license='None',
    packages=['graphite_paper'],
    python_requires='>=3.6',
    install_requires=[
        "Django",
        "Jinja2",
        "Markdown",
        "MarkupSafe",
        "numpy",
        "pandas",
        "python-dateutil",
        "pytz",
        "PyYAML",
        "six",
    ],
)
