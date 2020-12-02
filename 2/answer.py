#!/usr/bin/env python

import os

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


base_path = os.path.dirname(os.path.abspath(__file__))

input = open("%s/input" % base_path, "r").read().splitlines()

valid_policy_one = 0;

print("\n = Part One\n")

for row in input:
    data = parse(row)

    if is_valid_policy_one(**data):
        valid_policy_one += 1

print("Number of valid passwords are {} (of {} passwords)".format(valid_policy_one, len(input)))

print("\n = Part Two\n")

valid_policy_two = 0

for row in input:
    data = parse(row)

    if is_valid_policy_two(**data):
        valid_policy_two += 1

print("Number of valid passwords are {} (of {} passwords)".format(valid_policy_two, len(input)))
