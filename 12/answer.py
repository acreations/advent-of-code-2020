#!/usr/bin/env python

import sys

def movement(actions):

    directions = ['N', 'E', 'S', 'W']*2

    d = 'E'
    x = 0
    y = 0

    for a in actions:
        n = int(a[1:])

        if a[0] == 'E':
            x += n
        elif a[0] == 'N':
            y += n
        elif a[0] == 'W':
            x -= n
        elif a[0] == 'S':
            y -= n
        elif a[0] == 'F':
            if d in 'N':
                y += n
            elif d in 'E':
                x += n
            elif d in 'W':
                x -= n
            elif d in 'S':
                y -= n
        else:
            movement = int(int(n if 'R' == a[0] else -n) / 90)
            d = directions[directions.index(d) + movement]

    return abs(x) + abs(y)

def adv_movement(actions):

    wx = 10
    wy = 1

    x = 0
    y = 0

    for a in actions:

        n = int(a[1:])

        if a[0] == 'E':
            wx += n
        elif a[0] == 'N':
            wy += n
        elif a[0] == 'W':
            wx -= n
        elif a[0] == 'S':
            wy -= n
        elif a[0] == 'F':
            x += wx*n
            y += wy*n
        elif a[0]=='R':
          if   n==90:  wx,wy = wy,-wx
          elif n==180: wx,wy = -wx,-wy
          elif n==270: wx,wy = -wy,wx
        elif a[0]=='L':
          if   n==90:  wx,wy = -wy,wx
          elif n==180: wx,wy = -wx,-wy
          elif n==270: wx,wy = wy,-wx

    return abs(x) + abs(y)

input = open("{}/input".format(sys.path[0]), "r").read().splitlines()

print(open("{}/part_one".format(sys.path[0]), "r").read())

print("{}\nMy answer is {}\n{}".format("="*17, movement(input), "="*17))

print(open("{}/part_two".format(sys.path[0]), "r").read())

print("{}\nMy answer is {}\n{}".format("="*18, adv_movement(input), "="*18))
