#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2025-01-13
Purpose: Rock the Casbah
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-c',
                        '--num-chars',
                        help='Print number of chars',
                        action='store_true')

    parser.add_argument('-w',
                        '--num-words',
                        help='Print number of words',
                        action='store_true')

    parser.add_argument('-l',
                        '--num-lines',
                        help='Print number of lines',
                        action='store_true')

    return parser.parse_args()


def make_str(args, lines_in, words_in, bytes_in, name_in):
    c = False
    w = False
    li = False

    if args.num_chars:
        c = True
    if args.num_words:
        w = True
    if args.num_lines:
        li = True

    if (not c) and (not w) and (not li):
        c = True
        w = True
        li = True

    S = ' ' + name_in
    if c:
        S = '{:8}'.format(bytes_in) + S
    if w:
        S = '{:8}'.format(words_in) + S
    if li:
        S = '{:8}'.format(lines_in) + S

    return S


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    total_lines = 0
    total_words = 0
    total_bytes = 0

    for fh in args.file:
        num_lines = 0
        num_words = 0
        num_bytes = 0
        for line in fh:
            num_lines += 1
            num_words += len(line.split())
            num_bytes += len(line)

        S = make_str(args, num_lines, num_words, num_bytes, fh.name)
        print(f'{S}')

        total_lines += num_lines
        total_words += num_words
        total_bytes += num_bytes

    if len(args.file) > 1:
        S = make_str(args, total_lines, total_words, total_bytes, 'total')
        print(f'{S}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
