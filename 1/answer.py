#!/usr/bin/env python

import os

def correct_sum_of_2020(*n):
    return sum(n) == 2020

base_path = os.path.dirname(os.path.abspath(__file__))

input = list(map(int, open("{}/input".format(base_path), "r").read().split()))

print("\n = Part One \n")

for x in input:
    for y in input:
        if correct_sum_of_2020(x,y):
            print("{} + {} = 2020. Multiplying them is {}".format(x, y, (x*y)))

print("\n= Part Two \n")

for x in input:
    for y in input:
        for z in input:
            if correct_sum_of_2020(x,y,z):
                print("{} + {} + {}= 2020. Multiplying them is {}".format(x, y, z, (x*y*z)))
