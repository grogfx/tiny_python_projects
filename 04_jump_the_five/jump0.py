#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2024-12-30
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jump the five',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional', metavar='str', help='Input text')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    pos_arg = args.positional

    jumper = {
        '1': 'one',
        '2': 'two',
        '3': 'three',
        '4': 'four',
        '5': 'five',
        '6': 'six',
        '7': 'seven',
        '8': 'eight',
        '9': 'nine',
        '0': 'zero'
    }

    output = ''
    for char in pos_arg:
        output += jumper[char] + '-' if char in jumper else char
        output = output.replace('--', '-')
        output = output.replace('-.', '.')
        output = output.replace('- ', '.')

    print(output)

# --------------------------------------------------
if __name__ == '__main__':
    main()
