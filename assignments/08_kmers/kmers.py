#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-03-29
Purpose: Rock the Casbah
"""
import argparse
import io
from collections import defaultdict

# --------------------------------------------------
def get_args():
  """Get command-line arguments"""

  parser = argparse.ArgumentParser(
    description="Find common k-mers",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter,
  )

  # create arguments for file1, file2, k
  # make sure that k > 0
  # update the default arguments below

  parser = argparse.ArgumentParser(
    description='template',
    formatter_class=argparse.ArgumentDefaultsHelpFormatter)

  parser.add_argument('-k',
                      '--kmer',
                      help='A named integer argument',
                      metavar='int',
                      type=int,
                      default=3)

  parser.add_argument(
    'file1',
    help='Translated output file',
    metavar='FILE',
    type=argparse.FileType('rt'),
    default=None,
  )

  parser.add_argument(
    'file2',
    help='Translated output file',
    metavar='FILE',
    type=argparse.FileType('rt'),
    default=None,
  )

  args = parser.parse_args()
  if not 0 < args.kmer:
    parser.error(f'--kmer "{args.kmer}" must be > 0')

  return parser.parse_args()


# --------------------------------------------------
def main():
  """Find common k-mers"""

  args = get_args()
  words1 = count_kmers(args.file1, args.kmer)
  words2 = count_kmers(args.file2, args.kmer)

 # print('{:10s} {:>5s} {:>5s}'.format('Kmer', 'File1', 'File2'))

  for kmer in sorted(set(words1.keys()) & set(words2.keys())):
    print('{:10s} {:>5d} {:>5d}'.format(kmer, words1[kmer], words2[kmer]))

  # create a dictionary of kmers/counts in file1
  # create a dictionary of kmers/counts in file2
  # try using a function so you don't repeat code

  # find the intersection of the set of kmers
  # "common kmers" in kmers1 and kmers2


# --------------------------------------------------
def count_kmers(file, kmer_length):
  counts = {}
  for line in file:
    for word in line.split():
      for kmer in find_kmers(word, kmer_length):
        counts[kmer] = counts.get(kmer, 0) + 1
  return counts

def test_count_kmers():
  """Test count_kmers"""

  dat = "foo\nbar\nbaz\n"

  assert count_kmers(io.StringIO(dat), 3) == {"foo": 1, "bar": 1, "baz": 1}
  assert count_kmers(io.StringIO(dat), 2) == {
    "fo": 1,
    "oo": 1,
    "ba": 2,
    "ar": 1,
    "az": 1,
  }


# --------------------------------------------------
def find_kmers(seq, k):
  """Find k-mers in string"""

  n = len(seq) - k + 1
  return [] if n < 1 else [seq[i:i + k] for i in range(n)]


# --------------------------------------------------
def test_find_kmers():
  """Test find_kmers"""

  assert find_kmers("", 1) == []
  assert find_kmers("ACTG", 1) == ["A", "C", "T", "G"]
  assert find_kmers("ACTG", 2) == ["AC", "CT", "TG"]
  assert find_kmers("ACTG", 3) == ["ACT", "CTG"]
  assert find_kmers("ACTG", 4) == ["ACTG"]
  assert find_kmers("ACTG", 5) == []


# --------------------------------------------------
if __name__ == "__main__":
  main()
