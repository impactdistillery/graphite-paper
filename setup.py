from setuptools import setup


with open("readme.md", "r") as fh:
        long_description = fh.read()

setup(
    name='graphite-paper',
    version='0.0.1',
    description='Graphite Paper',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='http://www.impactdistillery.com/graphite',
    author='Larissa Wunderlich and Marcel Hebing',
    author_email='info@impactdistillery.com',
    license='None',
    packages=['graphite-paper'],
    python_requires='>=3.6',
)
