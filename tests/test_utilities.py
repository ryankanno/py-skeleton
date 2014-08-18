#!/usr/bin/env python
# -*- coding: utf-8 -*-

from jinja2 import Environment
from jinja2 import FileSystemLoader
from nose.tools import eq_
from nose.tools import ok_
from nose_parameterized import parameterized
import os
from py_skeleton.utilities import get_template_contents
from py_skeleton.utilities import resolve_templated_file_path
from py_skeleton.utilities import TEMPLATED_RE
import unittest


class TestUtilities(unittest.TestCase):

    def setUp(self):
        self.cwd = os.path.dirname(os.path.realpath(__file__))
        self.tmpl_dir = os.path.join(self.cwd, '.', 'data')

    def test_get_template_contents(self):
        loader = FileSystemLoader(self.tmpl_dir)
        env = Environment(loader=loader, keep_trailing_newline=True)
        context_dict = {"Default": {"Name": "Ryan"}}
        contents = get_template_contents(env, 'test.tmpl', context_dict)
        eq_(contents, "Hello, Ryan\n")

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
