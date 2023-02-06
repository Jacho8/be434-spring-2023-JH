#!/usr/bin/env python3
"""
Author : jasonhuynh <jasonhuynh@localhost>
Date   : 2023-02-03
Purpose: Create Sums
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Create Sums',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('int',
                        metavar= 'int',
                        type = int,
                        nargs = '+',
                        help='Numbers to add')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    int_arg = args.int
    num_ints = len(int_arg)
    
    result = sum(int_arg)
    equation = str(int_arg[0]) #output string of added integers

    #if else functions for differing numbers of arguments used 
    if num_ints == 1:
        print(f"{result} = {result}")
    else:
        for i in range(1,num_ints):
            equation = equation + " + " + str(int_arg[i])     
        print(f"{equation} = {result}")
   

    
# --------------------------------------------------
if __name__ == '__main__':
    main()
