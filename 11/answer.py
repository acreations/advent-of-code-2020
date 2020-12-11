#!/usr/bin/env python

import sys

def as_matrix(input):

    max_len = max([len(i) for i in input])

    matrix = [['.'] * (max_len + 2)]

    for row in input:
        matrix.append(['.'] + [r for r in row] + ['.'])

    matrix += [['.'] * (max_len + 2)]

    return matrix

def adjacent(matrix, x, y, endless=False):

    adj = []

    taken = []

    i = 1

    max_len_x = len(matrix)
    max_len_y = len(matrix[x]) - 1

    while i:

        if (x-i < 1 and y-i < 1 and x+i > max_len_x and y+i > max_len_y) or len(taken) == 9:
           break

        if x-i > 0 and not 'N' in taken and matrix[x-i][y] in ['L', '#']:
            adj += matrix[x-i][y]
            taken += ['N']

        if x+i < max_len_x and not 'S' in taken and matrix[x+i][y] in ['L', '#']:
            adj += matrix[x+i][y]
            taken += ['S']

        if y-i > 0 and not 'W' in taken and matrix[x][y-i] in ['L', '#']:
            adj += matrix[x][y-i]
            taken += ['W']

        if y+i < max_len_y and not 'E' in taken and matrix[x][y+i] in ['L', '#']:
            adj += matrix[x][y+i]
            taken += ['E']

        if x-i > 0 and y-i > 0 and not 'NW' in taken and matrix[x-i][y-i] in ['L', '#']:
            adj += matrix[x-i][y-i]
            taken += ['NW']

        if x-i > 0 and y+i < max_len_y and not 'NE' in taken and matrix[x-i][y+i] in ['L', '#']:
            adj += matrix[x-i][y+i]
            taken += ['NE']

        if x+i < max_len_x and y+i < max_len_y and not 'SE' in taken and matrix[x+i][y+i] in ['L', '#']:
            adj += matrix[x+i][y+i]
            taken += ['SE']

        if x+i < max_len_x and y-i > 0 and not 'SW' in taken and matrix[x+i][y-i] in ['L', '#']:
            adj += matrix[x+i][y-i]
            taken += ['SW']

        if not 'X' in taken and matrix[x][y] in ['L', '#']:
            adj += matrix[x][y]
            taken += ['X']

        i = i + 1 if endless else 0

    return adj


def predict(matrix):

    has_changes = False
    new_matrix = [m[:] for m in matrix]

    for x in range(1, len(matrix)-1):
        for y in range(1, len(matrix[x])-1):

            if matrix[x][y] == 'L':

                if adjacent(matrix, x, y).count('#') == 0:
                    new_matrix[x][y] = '#'

                    has_changes = True

            elif matrix[x][y] == '#':

                if adjacent(matrix, x, y).count('#') > 4:

                    new_matrix[x][y] = 'L'

                    has_changes = True

    return predict(new_matrix) if has_changes else new_matrix

def predict_extend(matrix):

    has_changes = False
    new_matrix = [m[:] for m in matrix]

    for x in range(1, len(matrix)-1):
        for y in range(1, len(matrix[x])-1):

            if matrix[x][y] == 'L':

                if adjacent(matrix, x, y, True).count('#') == 0:
                    new_matrix[x][y] = '#'

                    has_changes = True

            elif matrix[x][y] == '#':

                if adjacent(matrix, x, y, True).count('#') > 5:

                    new_matrix[x][y] = 'L'

                    has_changes = True


    return predict_extend(new_matrix) if has_changes else new_matrix

input = open("{}/input".format(sys.path[0]), "r").read().splitlines()

print(open("{}/part_one".format(sys.path[0]), "r").read())

matrix = predict(as_matrix(input))

print("{}\nMy answer is {}\n{}".format("="*17, sum([m.count('#') for m in matrix]), "="*17))

print(open("{}/part_two".format(sys.path[0]), "r").read())

matrix = predict_extend(as_matrix(input))

print("{}\nMy answer is {}\n{}".format("="*15, sum([m.count('#') for m in matrix]), "="*15))
