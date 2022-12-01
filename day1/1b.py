#!/usr/bin/env python3

print(sum(sorted([sum(list(map(int, x.split('\n')))) for x in open("input.txt").read().split("\n\n")], reverse=True)[0:3]))