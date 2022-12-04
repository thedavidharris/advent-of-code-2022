#!/usr/bin/env python3
import re

input = open('input.txt').read().splitlines()

total = 0
for line in input:
    a,b,c,d = map(int, re.findall('\d+', line))
    if a <= d and b >= c:
        total += 1

print(total)