#!/usr/bin/env python3
"""
Author : gmartins <gmartins@localhost>
Date   : 2025-01-13
Purpose: Rock the Casbah
"""

import argparse
import random


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Abuse',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-a',
                        '--adjectives',
                        metavar='adjectives',
                        default=2,
                        help='Number of adjectives',
                        type=int)

    parser.add_argument('-n',
                        '--number',
                        metavar='insults',
                        default=3,
                        help='Number of insults',
                        type=int)

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        default=None,
                        help='Random seed',
                        type=int)

    args = parser.parse_args()

    if args.adjectives < 1:
        parser.error(f'--adjectives "{args.adjectives}" must be > 0')

    if args.number < 1:
        parser.error(f'--number "{args.number}" must be > 0')

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    adjectives = """
        bankrupt
        base
        caterwauling
        corrupt
        cullionly
        detestable
        dishonest
        false
        filthsome
        filthy
        foolish
        foul
        gross
        heedless
        indistinguishable
        infected
        insatiate
        irksome
        lascivious
        lecherous
        loathsome
        lubbery
        old
        peevish
        rascaly
        rotten
        ruinous
        scurilous
        scurvy
        slanderous
        sodden-witted
        thin-faced
        toad-spotted
        unmannered
        vile
        wall-eyed
    """.split()

    nouns = """
        Judas
        Satan
        ape
        ass
        barbermonger
        beggar
        block
        boy
        braggart
        butt
        carbuncle
        coward
        coxcomb
        cur
        dandy
        degenerate
        fiend
        fishmonger
        fool
        gull
        harpy
        jack
        jolthead
        knave
        liar
        lunatic
        maw
        milksop
        minion
        ratcatcher
        recreant
        rogue
        scold
        slave
        swine
        traitor
        varlet
        villain
        worm
    """.split()

    args = get_args()

    random.seed(args.seed)

    for _ in range(args.number):
        a = ', '.join(random.sample(adjectives, k = args.adjectives))
        n = ''.join(random.choice(nouns))
        print(f'You {a} {n}!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
