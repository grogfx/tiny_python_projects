#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2025-01-13
Purpose: Rock the Casbah
"""

import argparse
import random
import os
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input',
                        metavar='input',
                        type=str,
                        help='text or file')

    parser.add_argument('-m',
                        '--mutations',
                        metavar='mutations',
                        default=0.1,
                        help='Percentage of mutations',
                        type=float)

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        default=None,
                        help='Random seed',
                        type=int)

    args = parser.parse_args()

    if os.path.isfile(args.input):
        args.input = open(args.input, 'rt', encoding='utf-8').read().rstrip()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    random.seed(args.seed)
    letter_bag = ''.join(sorted(string.ascii_letters + string.punctuation))
    line = args.input

    len_line = len(line)
    samples = random.sample(range(len_line),
                            k=round(args.mutations * len_line))

    def make_str(new_line, n):
        s_b = new_line[:n]
        s_a = new_line[n + 1:]
        s_c = random.choice(letter_bag.replace(new_line[n], ''))
        return s_b + s_c + s_a

    new_line = line
    for n in samples:
        new_line = make_str(new_line, n)

    print(f'You said: "{line.rstrip()}"')
    print(f'I heard : "{new_line.rstrip()}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
