#!/usr/bin/env python3
import re
from collections import defaultdict

input = open('input.txt').read().split('\n\n')

crates = input[0].splitlines()[:-1]
instructions = input[1].splitlines()

# Parse Stacks
stacks = defaultdict(list)
for line in crates:
    split_crates = re.findall('....?', line)
    for stack, crate in enumerate(split_crates):
        if not crate.isspace():
            stacks[stack + 1].append(crate[1])

# Parse Instructions
for line in instructions:
    num, from_stack, to_stack = map(int, re.findall('\d+', line))
    stacks[to_stack] = stacks[from_stack][:num][::-1] + stacks[to_stack]
    stacks[from_stack] = stacks[from_stack][num:]
    

print("".join([stacks[key][0] for key in sorted(stacks)]))
