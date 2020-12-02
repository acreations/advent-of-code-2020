#!/usr/bin/env python

import os

def parse(data):
    d = data.split()

    return {
        'min': int(d[0].split("-")[0]),
        'max': int(d[0].split("-")[1]),
        'policy': d[1][:1],
        'passwd': d[2]
    }

def is_valid(min, max, policy, passwd):

    counter = passwd.count(policy)

    return counter >= min and counter <= max

base_path = os.path.dirname(os.path.abspath(__file__))

input = open("%s/input" % base_path, "r").read().splitlines()

valid = 0;

for row in input:
    data = parse(row)

    if is_valid(**data):
        valid += 1

print("Number of valid passwords are {} (of {} passwords)a".format(valid, len(input)))
