#!/usr/bin/env python3
input = open('input.txt').read().split()

X = 1
strength = 0

for cycle, instruction in enumerate(input, 1):
    if cycle % 40 == 20:
        strength += cycle * X
    if instruction.lstrip('-+').isdigit():
        X += int(instruction)

print(strength)