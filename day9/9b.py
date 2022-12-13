#!/usr/bin/env python3
input = [line.split() for line in open('input.txt').read().splitlines()]

sign = lambda x: x and (1, -1)[x<0]

delta = {
        'U': 0 + 1j,
        'D': 0 -1j,
        'R': 1 + 0j,
        'L': -1 + 0j,
    }

knots = 2
rope = [complex(0,0)] * knots

visited = set()

for heading, distance in input:
    for i in range(int(distance)):
        rope[0] += delta[heading]

        for i in range(1,knots):
            diff = rope[i - 1] - rope[i]
            if abs(diff) >= 2:
                rope[i] += complex(sign(diff.real), sign(diff.imag))
        visited.add(rope[-1])

print(len(visited))