#!/usr/bin/env python


import sys


potions = {
    "A": 0,
    "B": 1,
    "C": 3,
}

def solve(input):
    return sum(potions[c] for c in input)


if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

