#!/usr/bin/env python

import sys

def jolt(input):

    jolt = []

    current = 0

    for i in range(0, len(input)):
        diff = input[i] - current

        jolt.append(diff)

        current = input[i]

    return jolt

def arrangements(input):

    cache = [0,0,1] + [0] * input[-1]

    for a in input:
        # a=1 corresponds to cache[3], so +2
        i = a + 2
        cache[i] = sum(cache[i-3:i])

    return cache[-1]

input = [int(i) for i in open("{}/input".format(sys.path[0]), "r").read().splitlines()]
input.sort()

print(open("{}/part_one".format(sys.path[0]), "r").read())

input.append(input[-1] + 3)

j = jolt(input)

print("{}\nMy answer is {}\n{}".format("="*17, (j.count(1) * j.count(3)), "="*17))

print(open("{}/part_two".format(sys.path[0]), "r").read())

print("{}\nMy answer is {}\n{}".format("="*15, arrangements(input), "="*15))
