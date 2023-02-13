#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-02-12
Purpose: DoReMi
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='DoReMi',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='str',
                        type = str,
                        nargs = '+',
                        help='Syllable Input')
    
    return parser.parse_args()

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    syll_arg = args.text
    
    solfege = dict(Do="A deer, a female deer",
                    Re="A drop of golden sun",
                    Mi="A name I call myself",
                    Fa="A long long way to run",
                    Sol="A needle pulling thread",
                    La="A note to follow sol",
                    Ti="A drink with jam and bread")

    for syllable in syll_arg:
        if syllable in solfege:
            print(f"{syllable}, {solfege[syllable]}")
        else:
            print(f"I don't know \"{syllable}\"")

# --------------------------------------------------
if __name__ == '__main__':
    main()
