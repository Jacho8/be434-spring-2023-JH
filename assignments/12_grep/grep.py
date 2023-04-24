#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-04-19
Purpose: Rock the Casbah
"""

import argparse
import re
import sys

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('pattern',
                        help='Search pattern')
    
    parser.add_argument('files',
                        nargs='+',
                        help='Input file(s)')

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout
                        )
    
    parser.add_argument('-i',
                        '--insensitive',
                        help='Case-insensitive search (default: False)',
                        action='store_true',
                        default=False
                        )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    pattern = re.compile(args.pattern, re.IGNORECASE if args.insensitive else 0)

    if len(args.files) > 1:
        for file in args.files:
            with open(file) as f:
                for line in f:
                    if pattern.search(line):
                        args.outfile.write(file + ':' + line)
    else:
        for file in args.files:
            with open(file) as f:
                for line in f:
                    if pattern.search(line):
                        args.outfile.write(line)


# --------------------------------------------------
if __name__ == '__main__':
    main()
