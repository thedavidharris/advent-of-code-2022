#!/usr/bin/env python3

print(max([sum(list(map(int, x.split('\n')))) for x in open("input.txt").read().split("\n\n")]))