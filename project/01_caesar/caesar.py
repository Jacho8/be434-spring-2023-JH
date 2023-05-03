#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-04-30
Purpose: Rock the Casbah
"""
import argparse
import sys
import string
import os
# --------------------------------------------------

letters = string.ascii_uppercase

'''  -h, --help            show this help message and exit
  -n NUMBER, --number NUMBER
                        A number to shift (default: 3)
  -d, --decode          A boolean flag (default: False)
  -o FILE, --outfile FILE
                        Output file (default: std.out)'''

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

    parser.add_argument('-n',
                        '--number',
                        help='A number to shift (default: 3)',
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

def shift_table(shift, decode=False): #Codify based on shift number

    table = {}
    
    for char in letters:
        index = letters.index(char)
        if not decode:
            shifted_index = (index + shift) % len(letters)
        else:
            shifted_index = (index - shift) % len(letters)
        shifted_char = letters[shifted_index]
        table[char] = shifted_char
    return table

def caesar(text, table): 
    
    cryptified = ""

    for char in text:
        if char.islower():
            shifted_char = table[char.upper()].lower()
        elif char.isupper():
            shifted_char = table[char]
        else:
            shifted_char = char
        cryptified += shifted_char.upper()

    print(cryptified)
    return cryptified

def read_file(filename):

    if os.path.isfile(filename.name):
        with filename as f:
            text = f.read().strip()
        return text

def write_file(text, filename=None):

    if filename:
        with open(filename.name, "w") as out_file:
            out_file.write(text)
    else:
        print(text)

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    table = shift_table(args.number, args.decode)
    text = read_file(args.file)

    if text:
        shifted = caesar(text, table)
        write_file(shifted, args.outfile)
    
    

# --------------------------------------------------
if __name__ == '__main__':
    main()
