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
        description='Emulate head',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--num-lines',
                        metavar='num_lines',
                        default=10,
                        help='Number of line(s)',
                        type=int)

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        n_line = 0
        for line in fh:
            n_line += 1
            if n_line > int(args.num_lines):
                break
            print(f'{line}', end='')


# --------------------------------------------------
if __name__ == '__main__':
    main()
