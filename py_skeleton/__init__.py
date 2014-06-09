#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from collections import namedtuple
version_info = namedtuple('version_info', ('major', 'minor', 'patch'))


VERSION = version_info(0, 0, 1)


__title__ = 'py_skeleton'
__version__ = '{0.major}.{0.minor}.{0.patch}'.format(VERSION)

__author__ = 'Ryan Kanno'
__copyright__ = 'Copyright 2014 Ryan Kanno'
__license__ = 'MIT'
__email__ = 'ryankanno@localkinegrinds.com'
__status__ = 'Development'

# vim: filetype=python
