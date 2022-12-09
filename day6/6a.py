#!/usr/bin/env python3
import re


input = open('input.txt').read()

for i in range(4,len(input)):
    packet = input[i-4:i]
    if len(set(packet)) == 4:
        print(i)
        break


