#!/usr/bin/env python

import sys

def count(group):
    return len(occurrances(group).keys())

def count_strict(group):
    strict = len(group.strip().split("\n"))
    return sum([1 if o == strict else 0 for o in occurrances(group).values()])

def occurrances(group):

    m = {}

    for g in group.split("\n"):
        for c in list(g):
            if not c in m:
                m[c] = 0
            m[c] += 1

    return m


input = open("{}/input".format(sys.path[0]), "r").read().split("\n\n")

print(open("{}/part_one".format(sys.path[0]), "r").read())

yes = sum([count(i) for i in input])

print("{}\nMy answer is {}\n{}".format("="*17, yes, "="*17))

print(open("{}/part_two".format(sys.path[0]), "r").read())

yes = sum([count_strict(i) for i in input])

print("{}\nMy answer is {}\n{}".format("="*15, yes, "="*15))
