#!/usr/bin/env python


import sys
import re


def find_runes(words, line):
    s = set()

    for word in words:
        for i in range(len(line)):
            rune = line[i:i+len(word)]
            if rune == word or rune == word[::-1]:
                for j in range(len(word)):
                    s.add(i+j)

    return s


def solve(input):
    [first,_,*second] = input.split("\n")
    words = first.split(":")[1].split(",")
    answer = 0

    for line in second:
        answer += len(find_runes(words, line))

    return answer



if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

