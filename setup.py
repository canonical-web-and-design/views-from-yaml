#! /usr/bin/env python3

from setuptools import setup

setup(
    name='canonicalwebteam.views-from-yaml',
    version='0.1.2',
    author='Canonical webteam',
    author_email='robin+pypi@canonical.com',
    url='https://github.com/canonical-webteam/views-from-yaml',
    packages=[
        'canonicalwebteam.views_from_yaml',
    ],
    description=(
        'A helper function for creating Django views from a YAML file of URL paths'
    ),
    long_description=open('README.rst').read(),
    install_requires=[
        'Django==1.3'
    ],
)

