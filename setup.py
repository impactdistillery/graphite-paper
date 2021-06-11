from setuptools import setup, find_packages

with open("readme.md", "r") as fh:
        long_description = fh.read()

setup(
    name='graphite-paper',
    version='0.0.6',
    description='Graphite Paper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://www.impactdistillery.com/graphite',
    author='Larissa Wunderlich and Marcel Hebing',
    author_email='info@impactdistillery.com',
    license='None',
    packages=find_packages(),
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
    include_package_data=True,
)
