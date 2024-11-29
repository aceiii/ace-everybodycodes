#!/usr/bin/env python


import sys
import re


def solve(input):
    nails = [int(line, 10) for line in input.split("\n")]
    lowest = min(nails)
    answer = sum(nail - lowest for nail in nails)
    return answer


if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

