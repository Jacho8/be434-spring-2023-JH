#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-02-19
Purpose: File reading
"""

import argparse
import os
import sys
import io

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='File reading',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('input_file',
                        metavar='FILE',
                        help='Input file(s)',
                        nargs='*',
                        type=argparse.FileType('rt'))

    parser.add_argument('-n',
                        '--number',
                        help='Text file line numbers',
                        action='store_true')

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        nargs='*',
                        default=[])

    args = parser.parse_args()

    for input_file in args.input_file:
        if os.path.isfile(input_file.name):
            args.file.append(input_file)
        else:
            return f"Error: '{input_file.name}' is not a valid file"

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    flag_arg = args.number

    if len(args.input_file) == 0:
        print('Error: No input files provided', file=sys.stderr)
    else:
        for text in args.file:
            if os.path.isfile(text.name):
                fh = open(text.name, 'rt')
                if flag_arg:
                    line_num = 1
                    '''for line in fh:
                        print(f"\t{line_num} {line.rstrip()}")
                        #print('%6s\t%s' % (line_num, line.rstrip()))'''
                    for line_num, line in enumerate(fh, start=1): # enumerate to tuple the line number and text together, allow for rjust to push whole statement
                        print(f"{str(line_num).rjust(6)}\t{line.rstrip()}")
                        line_num += 1
                else:
                    print(fh.read(), end='')
                fh.close()

# --------------------------------------------------
if __name__ == '__main__':
    main()