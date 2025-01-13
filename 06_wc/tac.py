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
        description='Emulate tac',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        nargs='*',
                        default=[sys.stdin],
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    for fh in args.file:
        for line in reversed(list(fh)):
            print(f'{line.rstrip()}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
