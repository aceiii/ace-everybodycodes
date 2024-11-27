#!/usr/bin/env python


import sys
import re


def solve(input):
    [first,_,second] = input.split("\n")
    words = first.split(":")[1].split(",")

    answer = 0
    for word in words:
        answer += len(re.findall(word, second)) 

    return answer


if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

