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
        '1': '9',
        '2': '8',
        '3': '7',
        '4': '6',
        '5': '0',
        '6': '4',
        '7': '3',
        '8': '2',
        '9': '1',
        '0': '5'
    }

    print(''.join([jumper.get(char, char) for char in pos_arg]))


# --------------------------------------------------
if __name__ == '__main__':
    main()
