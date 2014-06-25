#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import logging
import sys
import traceback
from .utilities import render_template_to_target


def init_argparser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('-s', '--source', action='store_true',
                        help='template source')
    parser.add_argument('-d', '--destination', action='store_true',
                        help='destination')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='increase chattiness of script')
    return parser


def do_work_son(args):
    loader = FileSystemLoader('/path/to/templates', followlinks=True)
    env = Environment(loader=loader)



def main(argv=None):
    if argv is None:
        argv = sys.argv

    parser = init_argparser()
    args = parser.parse_args(argv)

    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format=LOG_FORMAT)

    try:
        do_work_son(args)
    except:
        trace = traceback.format_exc()
        logging.error("OMGWTFBBQ: {0}".format(trace))
        sys.exit(1)

    # Yayyy-yah
    sys.exit(0)


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

# vim: filetype=python
