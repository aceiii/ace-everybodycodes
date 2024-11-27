#!/usr/bin/env python


import sys
import re


def build_map(input):
    rows = input.split("\n")
    height = len(rows)
    width = len(rows[0])
    return rows, (width, height)


def neighbours(pos):
    x, y = pos
    yield (x + 1, y)
    yield (x + 1, y + 1)
    yield (x, y + 1)
    yield (x - 1, y + 1)
    yield (x - 1, y)
    yield (x -1, y - 1)
    yield (x, y - 1)
    yield (x + 1, y - 1)


def dig_first_layer(dirt, dims):
    width, height = dims
    layer = []
    for y in range(height):
        for x in range(width):
            tile = dirt[y][x]
            if tile == "#":
                pos = (x, y)
                layer.append((pos, 1))
    return layer


def dig_secondary_layer(layer):
    pos_set = set(pos for pos, _ in layer)
    new_layer = []
    for pos, height in layer:
        neighbour_tiles = [next_pos for next_pos in neighbours(pos) if next_pos in pos_set]
        if len(neighbour_tiles) == 8:
            new_layer.append((pos, height + 1))
    return new_layer


def solve(input):
    dirt, dims = build_map(input)

    layer = dig_first_layer(dirt, dims)
    answer = len(layer)

    while True:
        layer = dig_secondary_layer(layer)
        count = len(layer)
        if not count:
            break
        answer += count

    return answer


if __name__ == "__main__":
    answer = solve(sys.stdin.read().strip())
    print(f"Answer: {answer}")

