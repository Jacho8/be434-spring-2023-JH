#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-04-20
Purpose: Rock the Casbah
"""

import argparse
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument(
                        'file1',
                        help='Input file 1',
                        metavar='FILE1',
                        type=argparse.FileType('rt')
                        )
    
    parser.add_argument(
                        'file2',
                        help='input file 2',
                        metavar='FILE2',
                        type=argparse.FileType('rt')
                        )
    
    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout
                        )
    

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    
    words1 = args.file1.read().split()
    words2 = args.file2.read().split()

    file1 = set(words1)
    file2 = set(words2)
    common = sorted(file1.intersection(words2))

    for word in common:
        print(word, file=args.outfile)

# --------------------------------------------------
if __name__ == '__main__':
    main()
