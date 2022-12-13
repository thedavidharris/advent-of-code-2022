#!/usr/bin/env python3
import math

input = open('input.txt').read().splitlines()

forest = [[int(x) for x in row] for row in input]
transposed_forest = list(zip(*forest))

score = 0

def view_length(tree, view):
    view_length = 0
    for v in view:
        view_length += 1
        if v >= tree:
            break
    return view_length

for i, row in enumerate(forest[0]):
    for j, height in enumerate(forest):
        tree = forest[i][j]

        lines = [
            forest[i][0:j][::-1],
            forest[i][j+1:],
            transposed_forest[j][0:i][::-1],
            transposed_forest[j][i+1:]
        ]

        score = max(score, math.prod([view_length(tree, line) for line in lines]))


print(score)


