#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2025-01-02
Purpose: Rock the Casbah
"""

import argparse
import os
import sys
import io
import pathlib


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler (upper case inputs)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        nargs='+',
                        type=str,
                        help='Input string or file')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    parser.add_argument('-e', '--ee', help='Lower case?', action='store_true')

    parser.add_argument('-d',
                        '--dir',
                        help='Output directory',
                        metavar='str',
                        default='output',
                        type=str)

    return parser.parse_args()


def action(string, lower=False):
    """Choose operation to transform input"""
    return string.lower() if lower else string.upper()


def exec_one_file(text, outfile_in, lower, multiple_files, dir_in):
    p = os.path.join(pathlib.Path.cwd(), dir_in)
    if not os.path.isdir(p):
        p = pathlib.Path(p)
        p.mkdir(exist_ok=True)

    if os.path.isfile(text) and multiple_files:
        outfile_in = os.path.join(os.path.abspath(dir_in),
                                  os.path.basename(text))
    elif (not os.path.isfile(text)) and multiple_files:
        return True

    outfile = open(outfile_in, 'wt',
                   encoding='utf-8') if outfile_in else sys.stdout

    with open(text, 'rt', encoding='utf-8') if os.path.isfile(
            text) else io.StringIO(text + '\n') as infile:
        for line in infile:
            outfile.write(action(line, lower))

    if outfile_in:
        outfile.close()

    return True


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text_arg = args.text
    outfile_arg = args.outfile
    lower_arg = args.ee
    dir_in = args.dir

    multiple_files = False
    if len(text_arg) > 1:
        multiple_files = True

    for file_in in text_arg:
        exec_one_file(file_in, outfile_arg, lower_arg, multiple_files, dir_in)

    return 0


# --------------------------------------------------
if __name__ == '__main__':
    main()
