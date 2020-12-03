#!/usr/bin/env python

import os

def collect(data, right, down):
    return [data[x*down][x*right] for x in range(1, int(len(data)/down))]

def multiply(list):
    result = 1
    for x in list:
        result *= x
    return result

base_path = os.path.dirname(os.path.abspath(__file__))

input = open("%s/input" % base_path, "r").read().splitlines()

# Expand it
input = [i*len(input) for i in input]

print("\n = Part One\n")

print("Number of trees are {}".format(collect(input, 3, 1).count("#")))

print("\n = Part Two\n")

trees = []
trees.append(collect(input, 1, 1).count("#"))
trees.append(collect(input, 3, 1).count("#"))
trees.append(collect(input, 5, 1).count("#"))
trees.append(collect(input, 7, 1).count("#"))
trees.append(collect(input, 1, 2).count("#"))

print("Number of trees are {}".format(multiply(trees)))
