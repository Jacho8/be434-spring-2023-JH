#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-02-26
Purpose: Read and translate text contents of file
"""

import argparse
import os
import sys
import io
from pprint import pprint

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Read and translate text contents of file',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('sequence',
                        metavar='sequence',
                        help='A positional argument')
    
    parser.add_argument('-c',
                        '--codons',
                        help='A named integer argument',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        required = 'True',
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='Translated output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.txt',
                        )           
                        

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    sequence = args.sequence.upper()
    codon_table = {}

    for line in args.codons:
        key, value = line.split()
        codon_table[key] = value
    protein = ''

    k = 3

    for codon in [sequence[i:i + k] for i in range(0, len(sequence), k)]:
        if codon in codon_table:
            protein += codon_table[codon]
        else:
            protein += '-'
    
    args.outfile.write(protein + '\n')
    args.outfile.close()

    print(f'Output written to "{args.outfile.name}".')


# --------------------------------------------------
if __name__ == '__main__':
    main()
