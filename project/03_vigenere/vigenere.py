#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-05-03
Purpose: Rock the Casbah
"""

import argparse
import sys
import os
import string

# --------------------------------------------------

alphabet = string.ascii_uppercase

''' -h, --help            show this help message and exit
  -k KEYWORD, --keyword KEYWORD
                        A keyword (default: CIPHER)
  -d, --decode          A boolean flag (default: False)
  -o FILE, --outfile FILE
                        Output file (default: std.out)
'''

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt')
                        )

    parser.add_argument('-k',
                        '--keyword',
                        help=' A keyword (default: CIPHER)',
                        metavar='str',
                        default='CIPHER')

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

def encode(plaintext, keyword):

    cipher = ''
    key_index = 0
    for char in plaintext:
        if char.isalpha():
            shift = alphabet.find(keyword[key_index].upper())
            key_index = (key_index + 1) % len(keyword)
            if char.isupper():
                cipher += alphabet[(alphabet.find(char) + shift) % 26]
            else:
                cipher += alphabet[(alphabet.find(char.upper()) + shift) % 26].lower()
        else:
            cipher += char

    return cipher

def decode(cipher, key):
    
    ogtext = ''
    key_len = len(key)
    index = [alphabet.index(key[i]) for i in range(key_len)]

    for i, char in enumerate(cipher):
        if char.isalpha():
            shift = index[i % key_len]
            char_index = alphabet.index(char.upper())
            char_shifted = (char_index - shift) % 26
            char_decrypted = alphabet[char_shifted]
            ogtext += char_decrypted
        else:
            ogtext += char

    return ogtext

def read_file(filename):
    if os.path.isfile(filename.name):
        with filename as f:
            text = f.read()
        return text.strip().upper()

def write_file(filename, input):

    if filename:
        with open(filename.name, "w") as out_file:
            out_file.write('\n'.join(input))
    else:
        print('\n'.join(input))

# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    input_text = read_file(args.file)

    if args.decode:
        translated_text = decode(input_text, args.keyword)
        print(translated_text)
    else:
        translated_text = encode(input_text, args.keyword)
        print(translated_text)

    write_file(args.outfile, [translated_text])

# --------------------------------------------------
if __name__ == '__main__':
    main()
