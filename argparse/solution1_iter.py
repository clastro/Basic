#!/usr/bin/env python3

#python3라는 interpreter 위치가 /usr/bin/env에 있다

""" Tetranucleotide frequency """

import argparse #argument를 관리하기 위한 library
import os
from typing import NamedTuple 
# Tuple은 immutable, 생성되면 값을 변경할 수 없음 : NamedTuple은 순서를 알아야할 때 사용


class Args(NamedTuple):
    """ Command-line arguments """
    dna: str


# --------------------------------------------------
def get_args() -> Args: #class 반환
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar='DNA', help='Input DNA sequence')

    args = parser.parse_args()

    if os.path.isfile(args.dna):
        args.dna = open(args.dna).read().rstrip()

    return Args(args.dna)


# --------------------------------------------------
def main() -> None: #아무것도 반환하지 않음
    """ Make a jazz noise here """

    args = get_args()
    count_a, count_c, count_g, count_t = 0, 0, 0, 0

    for base in args.dna:
        if base == 'A':
            count_a += 1
        elif base == 'C':
            count_c += 1
        elif base == 'G':
            count_g += 1
        elif base == 'T':
            count_t += 1

    print(count_a, count_c, count_g, count_t)


# --------------------------------------------------
if __name__ == '__main__':
    main()
