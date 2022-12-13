#!/usr/bin/env python3
input = open('input.txt').read().split()

X = 1
sprite = "\n"

for cycle, instruction in enumerate(input, 1):
    if (cycle-1) % 40 - X in [-1,0,1]:
        sprite += "#"
    elif cycle % 40 == 0:
        sprite += '\n'
    else:
        sprite += " "

    if instruction.lstrip('-+').isdigit():
        X += int(instruction)

print(sprite)