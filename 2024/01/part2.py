#!/usr/bin/env python


import sys
from itertools import pairwise


potions = {
    "x": 0,
    "A": 0,
    "B": 1,
    "C": 3,
    "D": 5,
}


def solve_pair(a, b):
    total = potions[a] + potions[b]
    if a != 'x' and b != 'x':
        return total + 2
    return total


def solve(input):
    return sum(solve_pair(a,b) for i, (a,b) in enumerate(pairwise(input)) if i % 2 == 0)


if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

