#!/usr/bin/env python

import sys

def control(preambles, number):
    for p in range(0, len(preambles)-1):
        for c in range(p+1, len(preambles)):
            if preambles[p] + preambles[c] == number and preambles[p] != preambles[c]:
                return 0
    return number

def contiguous(input, number):

    for p in range(0, len(input)-1):
        list = [input[p]]

        for c in input[p+1:]:
            list += [c]

            if sum(list) == number:
                return list
    return []


input = [int(i) for i in open("{}/input".format(sys.path[0]), "r").read().splitlines()]

print(open("{}/part_one".format(sys.path[0]), "r").read())

PRE_LEN = 25

controlled = [control(input[i-PRE_LEN:i], input[i]) for i in range(PRE_LEN, len(input))]

first = list(filter((0).__ne__, controlled))[0]

print("{}\nMy answer is {}\n{}".format("="*22, first, "="*22))

print(open("{}/part_two".format(sys.path[0]), "r").read())

contingous_list = contiguous(input[:controlled.index(first)], first)

sum = min(contingous_list) + max(contingous_list)

print("{}\nMy answer is {}\n{}".format("="*21, sum, "="*21))
