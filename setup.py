#!/usr/bin/env python

import sys
from setuptools import setup, find_packages

requires=[
    "boto",
    "Jinja2",
    "flask",
]

if sys.version_info[0] == 2 and sys.version_info[1] < 7:
    requires.append("ordereddict")

setup(
    name='moto',
    version='0.1.5',
    description='A library that allows your python tests to easily'
                ' mock out the boto library',
    author='Steve Pulec',
    author_email='spulec@gmail',
    url='https://github.com/spulec/moto',
    entry_points={
        'console_scripts': [
            'moto_server = moto.server:main',
        ],
    },
    packages=find_packages(),
    install_requires=requires,
)
