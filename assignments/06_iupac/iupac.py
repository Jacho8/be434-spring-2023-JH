#!/usr/bin/env python3
"""
Author : YOUR_NAME
Date   : TODAY'S DATE
Purpose: Expand IUPAC codes
"""
import argparse  #
import sys
import re

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    # create sequences and outfile arguments

    parser = argparse.ArgumentParser(
        description="template", formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "-f",
        "--file",
        help="A readable file",
        metavar="FILE",
        type=argparse.FileType("rt"),
        default=None,
    )
    parser.add_argument('-o',
                        '--outfile',
                        help='Translated output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout,
                        )
    parser.add_argument('SEQ',
                        help='Input Sequence',
                        metavar="str",
                        type=str,
                        nargs='+',
                        default=None,
                        )
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    trans = {
        "R": "[AG]",
        "Y": "[CT]",
        "S": "[GC]",
        "W": "[AT]",
        "K": "[GT]",
        "M": "[AC]",
        "B": "[CGT]",
        "D": "[AGT]",
        "H": "[ACT]",
        "V": "[ACG]",
        "N": "[ACGT]",
        "A": "A",
        "C": "C",
        "G": "G",
        "T": "T",
        "U": "U",
    }

    for seq in args.SEQ:
        t_seq = ""
        for iupac_code in seq:
            t_seq += trans[iupac_code.upper()]
        args.outfile.write(f'{seq} {t_seq}\n')
    #print(f'Done, see output in "{args.outfile.name}"')
    args.outfile.close()
# --------------------------------------------------
if __name__ == "__main__":
    main()
