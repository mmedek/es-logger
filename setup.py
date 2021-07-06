from os.path import join, dirname
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'es-logger/_version.py')) as f:
    exec(f.read())

setup(
    name='es-logger',
    version=version,
    description='Library for logging to Elastic Search.',
    long_description=open('README.md').read(),
    url='',
    author='Michal Medek',
    author_email='mmedek94@gmail.com',
    packages=find_packages(),
    keywords='logging, es, elastic search',
    install_requires=[
        'elasticsearch>=7.10.1'
    ],
    platforms=['any'],
    zip_safe=False
)