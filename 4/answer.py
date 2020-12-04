#!/usr/bin/env python

import re
import sys

def as_passport(data):
    passport = {}

    for d in data:
        tuple = d.split(":")

        passport[tuple[0]] = tuple[1]

    return passport

def as_passports_candidates(input):

    result = []

    passport_candidate = []

    for i in input:
        if i == '':
            result.append(as_passport(passport_candidate))
            passport_candidate = []
        else:
            for s in i.split():
                passport_candidate.append(s)

    # Last case
    result.append(as_passport(passport_candidate))

    return result

def to_valid_passports(passports):

    result = []

    keys = set(["byr","ecl","eyr","hcl","hgt","iyr","pid"])

    for p in passports:

        if keys.issubset(p.keys()):
            result.append(p)

    return result

def to_strict_passports(passports):

    result = []

    for p in passports:

        if int(p["byr"]) < 1920 or int(p["byr"]) > 2002:
            continue

        if int(p["iyr"]) < 2010 or int(p["iyr"]) > 2020:
            continue

        if int(p["eyr"]) < 2020 or int(p["eyr"]) > 2030:
            continue

        if p["hgt"]:

            if p["hgt"].endswith("cm"):
                control = int(p["hgt"][:-2])

                if control < 150 or control > 193:
                    continue

            elif p["hgt"].endswith("in"):
                control = int(p["hgt"][:-2])

                if control < 59 or control > 76:
                    continue

            else:
                continue

        if p["hcl"] and not re.match("^#[a-z0-9]{6}", p["hcl"]):
            continue

        if p["ecl"] and not p["ecl"] in ["amb","blu","brn","gry","grn","hzl","oth"]:
            continue

        if p["pid"] and not (re.match("^[0]*[0-9]*", p["hcl"]) and len(p["pid"]) == 9):
            continue

        result.append(p)

    return result

input = open("{}/input".format(sys.path[0]), "r").read().splitlines()

passport_candidates = as_passports_candidates(input)

valid_passports = to_valid_passports(passport_candidates)

print(open("{}/part_one".format(sys.path[0]), "r").read())

print("{}\nMy answer is {}\n{}".format("="*16, len(valid_passports), "="*16))

print(open("{}/part_two".format(sys.path[0]), "r").read())

strict_passports = to_strict_passports(valid_passports)

print("{}\nMy answer is {}\n{}".format("="*16, len(strict_passports), "="*16))
