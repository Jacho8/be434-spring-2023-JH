#!/usr/bin/env python3
"""
Author : YOUR_NAME
Date   : TODAY'S DATE
Purpose: Create synthetic sequences
"""

import argparse
import random

# --------------------------------------------------

'''* `-o`|`--outfile`: The output file to write the sequences (default "out.fa")
* `-t`|`--seqtype`: The sequence type, either `dna` or `rna` (`str`, default "dna")
* `-n`|`--numseqs`: The number of sequences to generate (`int`, default 10)
* `-m`|`--minlen`: The minimum length for any sequence (`int`, default 50)
* `-x`|`--maxlen`: The maximum length for any sequence (`int`, default 75)
* `-p`|`--pctgc`: The average percentage of GC content for a sequence (`float`, default 0.5 or 50%)
* `-s`|`--seed`: An integer value to use for the random seed (`int`, default `None`) so that the random choices of the program can be repeated under testing conditions.'''

def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-s',
                        '--seed',
                        help='An integer value to use for the random seed so that the random choices of the program can be repeated under testing conditions',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-t',
                        '--seqtype',
                        help='The sequence type',
                        metavar='str',
                        type=str,
                        choices=['dna', 'rna'],
                        default='dna')

    parser.add_argument('-n',
                        '--numseqs',
                        help='The number of sequences to generate',
                        metavar='int',
                        type=int,
                        default=10)

    parser.add_argument('-m',
                        '--minlen',
                        help='The minimum length for any sequence',
                        metavar='int',
                        type=int,
                        default=50)

    parser.add_argument('-x',
                        '--maxlen',
                        help='The maximum length for any sequence',
                        metavar='int',
                        type=int,
                        default=75)

    parser.add_argument('-o',
                        '--outfile',
                        help='Translated output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default='out.fa',
                        )

    parser.add_argument('-p',
                        '--pctgc',
                        help='The average percentage of GC content for a sequence',
                        metavar='float',
                        type=float,
                        default=0.5)

    args = parser.parse_args()
    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return parser.parse_args()

def create_pool(pctgc, max_len, seq_type):
    """ Create the pool of bases """

    t_or_u = 'T' if seq_type == 'dna' else 'U' 
    num_gc = int((pctgc / 2) * max_len)        
    num_at = int(((1 - pctgc) / 2) * max_len)  
    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at 

    for _ in range(max_len - len(pool)):       
        pool += random.choice(pool)

    return ''.join(sorted(pool))      

def test_create_pool():
    """ Test create_pool """

    state = random.getstate()
    random.seed(1)
    assert create_pool(.5, 10, 'dna') == 'AAACCCGGTT'
    assert create_pool(.6, 11, 'rna') == 'AACCCCGGGUU'
    assert create_pool(.7, 12, 'dna') == 'ACCCCCGGGGGT'
    assert create_pool(.7, 20, 'rna') == 'AAACCCCCCCGGGGGGGUUU'
    assert create_pool(.4, 15, 'dna') == 'AAAACCCGGGTTTTT'
    random.setstate(state)


# --------------------------------------------------
def main():
    """Make a jazz noise here"""
    args = get_args()

    random.seed(args.seed)
    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)
    type = args.seqtype
  
    for i in range(args.numseqs):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = ''.join(random.sample(pool, k=seq_len))
        seqid = f'seq-{i+1}'
        args.outfile.write(f'>{seqid} {type}\n{seq}\n')

    print(f"Done, wrote {args.numseqs} {args.seqtype.upper()} sequences to '{args.outfile.name}'.")


# --------------------------------------------------
if __name__ == '__main__':
    main()
