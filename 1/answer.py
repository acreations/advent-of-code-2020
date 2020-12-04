#!/usr/bin/env python

import sys

def correct_sum_of_2020(*n):
    return sum(n) == 2020

i = list(map(int, open("{}/input".format(sys.path[0]), "r").read().split()))

equal_size = int(len(i)/2)

print("")
print(open("{}/part_one".format(sys.path[0]), "r").read())

for x in range(0, equal_size):
    for y in range(equal_size, len(i)):
        if correct_sum_of_2020(i[x],i[y]):
            print("{}\nMy answer is {}\n{}".format("="*20, i[x]*i[y], "="*20))

print("")
print(open("{}/part_two".format(sys.path[0]), "r").read())

for x in i:
    for y in i:
        for z in i:
            if correct_sum_of_2020(x,y,z):
                print("{}\nMy answer is {}\n{}".format("="*23, x*y*z, "="*23))
                break
