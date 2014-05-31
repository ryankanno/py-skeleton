#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from collections import namedtuple
version_info = namedtuple('version_info', ('major', 'minor', 'patch'))


VERSION = version_info(0, 0, 1)


__title__ = ''
__version__ = '{0.major}.{0.minor}.{0.patch}'.format(VERSION)

__author__ = ''
__copyright__ = ''
__license__ = ''
__maintainer__ = ''
__email__ = ''
__status__ = 'Development'

# vim: filetype=python
