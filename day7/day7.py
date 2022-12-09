#!/usr/bin/env python3
import re
from pathlib import Path
from collections import Counter

input = open('input.txt').read().splitlines()

pwd = Path()
directories = Counter()

for line in input:
    match line.split():
        case ["$", "cd", name]:
            pwd = pwd.joinpath(name).resolve()
        case ['dir', _]:
            pass
        case ['$', 'ls']:
            pass
        case [size, name]:
            for path in [pwd, *pwd.parents]:
                directories[path] += int(size)



print("Part 1:", sum(value for value in directories.values() if value <= 100000))

space = directories[Path("/")] - 70000000 + 30000000
print("Part 2:", min(value for value in directories.values() if value >= space))


