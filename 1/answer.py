#!/usr/bin/env python

import sys

i = list(map(int, open("{}/input".format(sys.path[0]), "r").read().split()))

equal_size = int(len(i)/2)

print("")
print(open("{}/part_one".format(sys.path[0]), "r").read())

for x in range(0, equal_size-1):
    for y in range(equal_size, len(i)):
        if i[x] + i[y] == 2020:
            print("{}\nMy answer is {}\n{}".format("="*20, i[x]*i[y], "="*20))

print("")
print(open("{}/part_two".format(sys.path[0]), "r").read())

equal_size = int(len(i)/3)

for x in range(0, equal_size-1):
    for y in range(equal_size, equal_size*2-1):
        for z in range(equal_size, len(i)):
            if i[x] + i[y] + i[z] == 2020:
                print("{}\nMy answer is {}\n{}".format("="*22, i[x]*i[y]*i[z], "="*22))
