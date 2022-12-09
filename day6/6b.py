#!/usr/bin/env python3
import re


input = open('input.txt').read()

for i in range(14,len(input)):
    packet = input[i-14:i]
    if len(set(packet)) == 14:
        print(i)
        break


