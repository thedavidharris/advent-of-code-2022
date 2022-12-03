#!/usr/bin/env python3
from string import ascii_letters

input = open('input.txt').read().splitlines()

result = 0
for line in input:
    firstpart, secondpart = line[:len(line)//2], line[len(line)//2:]
    common = set(firstpart).intersection(set(secondpart)).pop()
    result += ascii_letters.index(common) + 1
print(result)