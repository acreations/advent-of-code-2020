#!/usr/bin/env python

import sys

def count(group):

    l = []

    for g in group.split("\n"):
        l += list(g)

    return len(set(l))


input = open("{}/input".format(sys.path[0]), "r").read().split("\n\n")

print(open("{}/part_one".format(sys.path[0]), "r").read())

yes = sum([count(i) for i in input])

print("{}\nMy answer is {}\n{}".format("="*17, yes, "="*17))

print(open("{}/part_two".format(sys.path[0]), "r").read())
