#!/usr/bin/env python
# -*- coding: utf-8 -*-

import fnmatch
import os
from py_utilities.fs.file_utilities import iter_files
from py_utilities.fs.file_utilities import write_file


def render_template_to_target(env, tmpl_src, context_dict, tmpl_target):
    tmpl = env.get_template(tmpl_src)
    contents = tmpl.render(context_dict)
    write_file(tmpl_target, contents)


def iter_files_filter(dir_path, filter_pattern):
    for file in iter_files(dir_path):
        if fnmatch.fnmatch(os.path.basename(file), filter_pattern):
            yield file


# vim: filetype=python
