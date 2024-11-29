#!/usr/bin/env python


import sys
import re


def solve_to(nails, level):
    return sum(abs(nail - level) for nail in nails)


def solve(input):
    nails = [int(line, 10) for line in input.split("\n")]
    results = [solve_to(nails, nail) for nail in nails]
    return min(results)


if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

