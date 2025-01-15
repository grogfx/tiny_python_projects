#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2025-01-13
Purpose: Rock the Casbah
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text', metavar='text', help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        metavar='vowel',
                        help='Vowel to change',
                        default='a',
                        choices=list('aieou'),
                        type=str)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    S = args.text
    for vowel_t in 'aeiouAEIOU':
        to_char = args.vowel
        if vowel_t.isupper():
            to_char = to_char.upper()
        S = S.replace(vowel_t, to_char)
    print(f'{S}')


# --------------------------------------------------
if __name__ == '__main__':
    main()
