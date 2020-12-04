#!/usr/bin/env python

import sys

def collect(data, right, down):
    return [data[x*down][x*right] for x in range(1, int(len(data)/down))]

def multiply(list):
    result = 1
    for x in list:
        result *= x
    return result


input = open("{}/input".format(sys.path[0]), "r").read().splitlines()

# Expand it
input = [i*len(input) for i in input]

print(open("{}/part_one".format(sys.path[0]), "r").read())

print("{}\nMy answer is {}\n{}".format("="*16, collect(input, 3, 1).count("#"), "="*16))

print(open("{}/part_two".format(sys.path[0]), "r").read())

trees = []
trees.append(collect(input, 1, 1).count("#"))
trees.append(collect(input, 3, 1).count("#"))
trees.append(collect(input, 5, 1).count("#"))
trees.append(collect(input, 7, 1).count("#"))
trees.append(collect(input, 1, 2).count("#"))

print("{}\nMy answer is {}\n{}".format("="*23, multiply(trees), "="*23))
