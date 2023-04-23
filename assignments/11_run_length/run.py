#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-04-11
Purpose: Rock the Casbah
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        help='DNA text or file'
                        )
    
    return parser.parse_args()

def rle(seq):
    
    prev = ""
    encoded = ""
    i = 1

    for char in seq:
        if char != prev:
            if prev:
                encoded += prev + ("" if i == 1 else str(i))
            i = 1
            prev = char
        else:
            i += 1

    if prev:
        encoded += prev + ("" if i == 1 else str(i))

    return encoded



# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    text = args.text

    if os.path.isfile(text):
        with open(text) as fh:
            for line in fh:
                line = line.rstrip()
                print(rle(line))
    else:
        print(rle(text))



# --------------------------------------------------
if __name__ == '__main__':
    main()
