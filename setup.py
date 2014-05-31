#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

packages = []
requires = []

with open('README.rst') as f:
    readme = f.read()

with open('CHANGES') as f:
    changes = f.read()

classifiers = [
]

setup(
    name='',
    version='',
    description='',
    long_description=readme + '\n\n' + changes,
    author='',
    author_email='',
    url="",
    packages=packages,
    package_data={'': ['LICENSE']},
    package_dir={'': ''},
    install_requires=[],
    license='MIT',
    tests_require=[],
    classifiers=classifiers,
)

# vim: filetype=python
