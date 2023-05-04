#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-05-01
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import string
import random
# --------------------------------------------------

alphabet = string.ascii_uppercase

'''optional arguments:
  -h, --help            show this help message and exit
  -s SEED, --seed SEED  A random seed (default: 3)
  -d, --decode          A boolean flag (default: False)
  -o FILE, --outfile FILE Output file (default: std.out)'''

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE1',
                        type=argparse.FileType('rt')
                        )

    parser.add_argument('-s',
                        '--seed',
                        help='A random seed (default: 3)',
                        metavar='int',
                        type=int,
                        default=3)

    parser.add_argument('-d',
                        '--decode',
                        help='A boolean flag (default: False)',
                        action="store_true")

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout
                        )

    return parser.parse_args()

def scramble(seed):

    random.seed(seed)
    scramble_alphabet = ''.join(random.sample(alphabet, len(alphabet)))

    return scramble_alphabet

def encode(message, scramble_alphabet):

    translation = str.maketrans(alphabet, scramble_alphabet)
    
    return message.translate(translation)

def decode_message(message, scramble_alphabet):

    translation = str.maketrans(scramble_alphabet, alphabet)
   
    return message.translate(translation)

def process_file(lines, scramble_alphabet, decoded):
    
    encoded_lines = []
    for line in lines:
        if decoded:
            encoded_lines.append(decode_message(line, scramble_alphabet))
        else:
            encoded_lines.append(encode(line, scramble_alphabet))
    return '\n'.join(encoded_lines)

def read_file(filename):

    if os.path.isfile(filename.name):
        with filename as f:
            lines = f.readlines()

        return [line.strip().upper() for line in lines]

def write_file(encoded_lines, filename=None):

    if filename:
        with open(filename.name, "w") as out_file:
            out_file.write('\n'.join(encoded_lines))
    else:
        print('\n'.join(encoded_lines))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    code_seed = args.seed

    lines = read_file(args.file)
    scrambled = scramble(code_seed)
    encoded_lines = process_file(lines,scrambled,args.decode)

    print(encoded_lines)

    if args.outfile:
        write_file('\n'.join(encoded_lines), args.outfile)
    else:
        print(''.join(encoded_lines))

# --------------------------------------------------
if __name__ == '__main__':
    main()
