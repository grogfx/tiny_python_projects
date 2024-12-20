#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2024-12-17
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word', metavar='word', help='A word')

    parser.add_argument('-s',
                        '--side',
                        metavar='side',
                        help='larboard or starboard',
                        default='larboard')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word

    if word.isalpha():
        article = 'an' if word[0].lower() in 'aeiou' else 'a'
        article = article.title() if word[0].isupper() else article
        side = 'starboard' if args.side == 'right' else 'larboard'
        print(f'Ahoy, Captain, {article} {word} off the {side} bow!')
    else:
        print('Invalid word')


# --------------------------------------------------
if __name__ == '__main__':
    main()
