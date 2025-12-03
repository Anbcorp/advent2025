#!/usr/bin/env python3

import copy
import sys

fname = sys.argv[1]
with open(fname, 'r') as input:
    total = 0
    for line in input.readlines():
        i = []
        line = line.strip()
        print(f"line is {line}")
        m = max(line)
        mi = line.index(m)
        print(f"  max is {m} at {mi}")
        i.append(mi)
        if i[0] == len(line)-1:
            print(f"  max is last")
            m = max(line[:-1])
            mi = line.index(m)
            print(f"    othermax is {m} at {mi}")
            # Reverse order
            i.append(i[0])
            i[0] = mi
        else:
            print(f"  max is somewhere")
            m = max(line[i[0]+1:])
            mi = line[i[0]+1:].index(m)
            # Can't use line[i[0]+1:] index in line directly, rebase index
            mi += i[0]+1
            print(f"    othermax is {m} at {mi}")
            i.append(mi)

        total+= int(line[i[0]]+line[i[1]])
        print(f"{line[i[0]]}{line[i[1]]} total is {total}")


"""
New approach :
Find max.
if max is last elem
    find othermax on line[:-1]
else
    find othermax on line[index_max]
"""

