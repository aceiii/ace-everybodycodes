#!/usr/bin/env python


import sys
import re


def line_horizontal(lines, pos, n):
    x, y = pos
    w = len(lines[y])
    return [((x+i)%w, y) for i in range(n)]


def line_vertical(lines, pos, n):
    x, y = pos
    h = len(lines)
    res = [(x,y+i) for i in range(n) if y+i < h]
    return res


def word_from(lines, positions):
    chars = []
    for (x,y) in positions:
        chars.append(lines[y][x])
    return "".join(chars)


def words_at(lines, pos, n): 
    hor = line_horizontal(lines, pos, n)
    hor_word = word_from(lines, hor)
    yield hor_word, hor

    ver = line_vertical(lines, pos, n)
    ver_word = word_from(lines, ver)
    yield ver_word, ver


def find_runes_at(pos, words, lines):
    s = set()
    for word in words:
        for rune, scales in words_at(lines, pos, len(word)):
            if rune == word:
                s = s.union(scales)
    return s


def find_scales(words, lines):
    word_set = set()
    scale_set = set()

    for word in words:
        word_set.add(word)
        word_set.add(word[::-1])

    for y,line in enumerate(lines):
        for x in range(len(line)):
            scale_set = scale_set.union(find_runes_at((x, y), word_set, lines))

    return scale_set


def solve(input):
    [first,_,*second] = input.split("\n")
    words = first.split(":")[1].split(",")
    answer = 0
    res = find_scales(words, second)
    return len(res)


if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

