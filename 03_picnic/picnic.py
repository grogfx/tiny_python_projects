#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2024-12-18
Purpose: Rock the Casbah
"""

import argparse

TEMPLATE = 'You are bringing {}.'


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Picnic game',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        nargs='+',
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items',
                        action='store_true')

    parser.add_argument('-n',
                        '--not-oxford',
                        help='Do not print Oxford comma',
                        action='store_true')

    parser.add_argument('-r',
                        '--sep',
                        metavar='separator',
                        default=',',
                        help='Separator')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sorted_arg = args.sorted

    pos_arg = args.positional
    oxford_arg = args.not_oxford
    sep_arg = args.sep + ' '

    if sep_arg != ', ':
        oxford_arg = True

    if sorted_arg:
        pos_arg.sort()

    if len(pos_arg) < 1:
        print('Error')
    elif len(pos_arg) == 1:
        print(TEMPLATE.format(pos_arg[0]))
    else:
        if len(pos_arg) == 2:
            s = ' and '.join(pos_arg)
        else:
            pos_arg[-1] = 'and ' + pos_arg[-1]
            s = sep_arg.join(pos_arg)
            if oxford_arg:
                s = s.replace(sep_arg + 'and', ' and')
        print(TEMPLATE.format(s))


# --------------------------------------------------
if __name__ == '__main__':
    main()
