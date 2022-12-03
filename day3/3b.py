#!/usr/bin/env python3
from more_itertools import chunked
from string import ascii_letters

input = open('input.txt').read().splitlines()

result = 0
for line in chunked(input, 3):
    a, b, c = line
    common = set(a).intersection(set(b)).intersection(set(c)).pop()
    result += ascii_letters.index(common) + 1
print(result)