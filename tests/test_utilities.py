#!/usr/bin/env python
# -*- coding: utf-8 -*-

from nose.tools import ok_
from nose_parameterized import parameterized
from py_skeleton.utilities import resolve_templated_file_path
from py_skeleton.utilities import TEMPLATED_RE
import unittest


class TestUtilities(unittest.TestCase):

    @parameterized.expand([
        ("/foo/bar"),
        ("/foo/bar/{foo}"),
        ("/foo/bar/{{foo"),
        ("/foo/bar/{foo}}")
    ])
    def test_tmpl_regular_expression_with_invalid_template_paths(self, path):
        m = TEMPLATED_RE.search(path)
        ok_(m is None)

    @parameterized.expand([
        ("/foo/bar/{{temp}}", "temp"),
        ("/foo/bar/{{temp.bar}}", "temp.bar"),
        ("/foo/bar/{{     temp.bar}}", "temp.bar"),
    ])
    def test_tmpl_regular_expression_with_valid_template_paths(
            self, path, config_key):
        m = TEMPLATED_RE.search(path)
        if m:
            ok_(m.group(2).strip() == config_key)

    def test_resolve_templated_file_path_with_no_match_returns_self(self):
        path = "/foo/bar/is/not/templated"
        ok_(path, resolve_templated_file_path(path, None))

# vim: filetype=python
