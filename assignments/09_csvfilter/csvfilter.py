#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-04-02
Purpose: Rock the Casbah
"""

import argparse
import csv
import sys
import re

# --------------------------------------------------
"""
* `-f`|`--file`: A *required* argument that is a readable file
* `-v`|`--val`: A *required* "value" to match against each record
* `-c`|`--col`: An optional "column" to search for the given value
* `-o`|`--outfile`: An optional output file name (default `'out.csv'`)
* `-d`|`--delimiter`: An optional delimiter to use to parse the file (default `','`)
"""
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-v',
                        '--val',
                        help='A *required* "value" to match against each record',
                        metavar='str',
                        type=str,
                        required = True,
                        default=None)

    parser.add_argument('-c',
                        '--col',
                        help='An optional "column" to search for the given value',
                        metavar='str',
                        type=str,
                        default=None)

    parser.add_argument('-f',
                        '--file',
                        help='A readable file',
                        metavar='FILE',
                        required = True,
                        type=argparse.FileType('rt'),
                        default=None)

    parser.add_argument('-o',
                        '--outfile',
                        help='A readable file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.csv')
    
    parser.add_argument('-d',
                        '--delimiter',
                        help='An optional delimiter to use to parse the file',
                        metavar='str',
                        type=str,
                        default=',')
    
    args = parser.parse_args()

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    with open(args.file.name, 'rt', newline='') as csvfile:
        reader = csv.DictReader(csvfile, delimiter=args.delimiter)
        fieldnames = reader.fieldnames

        if args.col not in fieldnames: # Verify column is valid
            print(f'--col "{args.col}" not a valid column!')
            print(f'Choose from {", ".join(fieldnames)}')
            exit(1)

        with open(args.outfile.name, 'wt', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()

            csvfile.seek(0)
            num = 0
            for rec in reader:
                if args.col:
                    text = rec[args.col]
                else:
                    text = ",".join(rec.values())
                if re.search(args.val, text, re.IGNORECASE):
                    writer.writerow(rec)
                    num += 1
                """else: # exception case when col default is specified to a header
                    if any(re.search(args.val, v, re.IGNORECASE) for v in rec.values()):
                        writer.writerow(rec)
                        num += 1"""

    print(f"Done, wrote {num} to \"{args.outfile.name}\".")


# --------------------------------------------------
if __name__ == '__main__':
    main()
