#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2025-01-13
Purpose: Learning
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Emulate wc (word count)',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+',
                        help='Input letter(s)',
                        type=str)

    parser.add_argument('-f',
                        '--file',
                        metavar='FILE',
                        nargs='?',
                        default='gashlycrumb.txt',
                        help='Input file(s)',
                        type=argparse.FileType('rt'))

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    fh = args.file

    d = {line[0].upper(): line.rstrip() for line in fh}

    for letter in args.letter:
        print(d.get(letter.upper(), f'I do not know "{letter}".'))


# --------------------------------------------------
if __name__ == '__main__':
    main()
