#!/usr/bin/env python

import sys

def normalize(text):
    return text.replace("bags", "").replace("bag","").replace(".","").strip()

def rules(input):

    rules = {}

    for i in input:
        s = i.split(" contain ")

        rule = normalize(s[0])

        rules[rule] = []

        if s[1] != "no other bags.":
            for j in s[1].split(', '):
                rules[rule].append({ 'qty': int(j[:1]), 'rule': normalize(j[2:]) })

    return rules

def count_shiny_bag(rules, r, qty=1):

    if r == 'shiny gold':
        return qty

    elif not r in rules:
        return 0

    return sum([count_shiny_bag(rules, r['rule'], qty*r['qty']) for r in rules[r]])

def count_bags(rules, r, qty=1):

    if not rules[r]:
        return qty

    return sum([count_bags(rules, r['rule'], qty*r['qty']) for r in rules[r]]) + qty

input = open("{}/input".format(sys.path[0]), "r").read().splitlines()

print(open("{}/part_one".format(sys.path[0]), "r").read())

rules = rules(input)

shiny_bags = [count_shiny_bag(rules, r) for r in rules]

print("{}\nMy answer is {}\n{}".format("="*17, sum([s > 0 for s in shiny_bags])-1, "="*17))

print(open("{}/part_two".format(sys.path[0]), "r").read())

count_bags = count_bags(rules, 'shiny gold') - 1

print("{}\nMy answer is {}\n{}".format("="*18, count_bags, "="*18))
