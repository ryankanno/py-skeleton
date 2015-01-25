#!/usr/bin/env python
# -*- coding: utf-8 -*-

import errno
import fnmatch
import io
import os
import re

TEMPLATED_RE = re.compile(r'(\{\{([\w\s\.]+)\}\})')


def render_template_to_target(
        env,
        tmpl_src,
        context_dict,
        tmpl_target,
        tmpl_ext):

    contents = get_template_contents(env, tmpl_src, context_dict)
    _mkdir_p(os.path.dirname(tmpl_target))

    with io.open(tmpl_target.replace(tmpl_ext, ''), 'w') as f:
        f.write(contents)


def resolve_templated_file_path(templated_file_path, config):
    match = TEMPLATED_RE.search(templated_file_path)
    if match:
        templated_value = config.get(match.group(2))
        if templated_value:
            return templated_file_path.replace(match.group(1), templated_value)
    return templated_file_path


def iter_files_filter(dir_path, filter_pattern):
    for file in _iter_files(dir_path):
        if fnmatch.fnmatch(os.path.basename(file), filter_pattern):
            yield file


def get_template_contents(env, tmpl_src, context_dict):
    tmpl = env.get_template(tmpl_src)
    return tmpl.render(context_dict)


def _iter_files(src_dir, **walk_args):
    """
    Returns a iterator to walk the files in `src_dir`. You can provide
    additional arguments to `os.walk` via `walk_args`.
    """
    for root, dirs, files in os.walk(src_dir, walk_args):
        for f in files:
            yield os.path.join(root, f)


def _mkdir_p(path):
    """
    Recursive directory creation function. Mimics `mkdir -p`. Doesn't
    raise an error if the leaf exists and is a directory.

    Reference: http://stackoverflow.com/questions/600268/\
    mkdir-p-functionality-in-python/600612#600612
    """
    try:
        os.makedirs(path)
    except OSError as exc:
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise

# vim: filetype=python
