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

mult = {
    1: 0,
    2: 1,
    3: 2,
}


def potion_count(a, n):
    if a == 'x':
        return 0
    return potions[a] + mult[n]


def solve(input):
    total = 0
    for i in range(0, len(input), 3):
        group = input[i:i+3]
        n = 3 - group.count('x')
        total += sum(potion_count(a, n) for a in group)
    return total


if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

