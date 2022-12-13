#!/usr/bin/env python3
input = open('input.txt').read().splitlines()

forest = [[int(x) for x in row] for row in input]
transposed_forest = list(zip(*forest))

visible = 0

for i, row in enumerate(forest[0]):
    for j, height in enumerate(forest):
        tree = forest[i][j]

        lines = [
            forest[i][0:j][::-1],
            forest[i][j+1:],
            transposed_forest[j][0:i][::-1],
            transposed_forest[j][i+1:]
        ]

        if any([all(x < tree for x in line) for line in lines]):
            visible += 1

print(visible)


