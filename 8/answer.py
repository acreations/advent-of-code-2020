#!/usr/bin/env python

import sys

def accumulator(input, index=0, store={}):

    if index in store or index >= len(input):
        return store

    store[index] = 0

    new_index = index + 1

    line = input[index].split()

    if line[0] == 'acc':
        store[index] += int(line[1])
    elif line[0] == 'jmp':
        new_index = index + int(line[1])

    return accumulator(input, new_index, store)

def fix_accumulator(input):
    for i in range(0, len(input)):
        line = input[i].split()

        if line[0] in ['nop', 'jmp']:
            updated = input[:]
            updated[i] = '{} {}'.format(('jmp' if line[0] == 'nop' else 'nop'), line[1])

            acc = accumulator(updated, 0, {})

            if max(acc) == (len(input)-1):
                return acc
    return {}


input = open("{}/input".format(sys.path[0]), "r").read().splitlines()

print(open("{}/part_one".format(sys.path[0]), "r").read())

print("{}\nMy answer is {}\n{}".format("="*17, sum(accumulator(input).values()), "="*17))

print(open("{}/part_two".format(sys.path[0]), "r").read())

print("{}\nMy answer is {}\n{}".format("="*17, sum(fix_accumulator(input).values()), "="*17))
