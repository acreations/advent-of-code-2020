#!/usr/bin/env python

import sys

def parse(data):
    d = data.split()

    return {
        'a': int(d[0].split("-")[0]),
        'b': int(d[0].split("-")[1]),
        'policy': d[1][:1],
        'passwd': d[2]
    }

def is_valid_policy_one(a, b, policy, passwd):

    counter = passwd.count(policy)

    return counter >= a and counter <= b

def is_valid_policy_two(a, b, policy, passwd):

    match_pos_one = passwd[a-1] == policy
    match_pos_two = passwd[b-1] == policy

    return (match_pos_one or match_pos_two) and not (match_pos_one and match_pos_two)

input = open("{}/input".format(sys.path[0]), "r").read().splitlines()

valid_policy_one = 0;

print(open("{}/part_one".format(sys.path[0]), "r").read())

for row in input:
    data = parse(row)

    if is_valid_policy_one(**data):
        valid_policy_one += 1

print("{}\nMy answer is {}\n{}".format("="*16, valid_policy_one, "="*16))

print(open("{}/part_two".format(sys.path[0]), "r").read())


valid_policy_two = 0

for row in input:
    data = parse(row)

    if is_valid_policy_two(**data):
        valid_policy_two += 1

print("{}\nMy answer is {}\n{}".format("="*16, valid_policy_two, "="*16))
