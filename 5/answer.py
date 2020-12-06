#!/usr/bin/env python

import sys

def seats(code):

    row = decode(code[0:7], 0, "F", 127, "B")
    col = decode(code[7:], 0, "L", 7, "R")

    return { "row": row, "col": col, "seat_id": row * 8 + col }

def decode(code, min, min_code, max, max_code):

    new_min = min if code[0] == min_code else min + (max - min + 1)/2
    new_max = max if code[0] == max_code else max - (max - min + 1)/2

    if len(code) == 1:
        return int(new_max) if code[0] == max_code else int(new_min)

    return decode(code[1:], new_min, min_code, new_max, max_code)


input = open("{}/input".format(sys.path[0]), "r").read().splitlines()

print(open("{}/part_one".format(sys.path[0]), "r").read())

seats = [seats(c) for c in input]
seats_ids = [s["seat_id"] for s in seats]

print("{}\nMy answer is {}\n{}".format("="*16, max(seats_ids), "="*16))

print(open("{}/part_two".format(sys.path[0]), "r").read())

seats_ids.sort()

for s in range(seats_ids[0], seats_ids[-1]):
    if not s in seats_ids:
        print("{}\nMy answer is {}\n{}".format("="*16, s, "="*16))
