#!/usr/bin/env python3

import copy
import sys

fname = sys.argv[1]
with open(fname, 'r') as input:
    for line in input.readlines():
        indexes = []
        line = line.strip()
        workline = list(copy.copy(line))
        indexes.append(line.index(max(workline)))
        # This changes the indexes and create off by one error
        workline.pop(indexes[-1])
        indexes.append(line.index(max(workline)))
        si = sorted(indexes)
        if line[si[1]] > line[si[0]]:
            """ Try to find another maximum starting after si[1] """
            try:
                nm = max(line[si[1]+1])
                print(f"{si[1]+1} is {line[si[1]+1]}")
            except IndexError:
                # Already at max, continue
                pass
            else:
                si[0]=si[1]
                si[1] = line.index(nm)

        print(line[si[0]], line[si[1]])


        """ If i2 > i1, look for next maximum after i2, unless i2 == length
        """
"""
New approach :
Find max.
if max is last elem
    find othermax on line[:-1]
else
    find othermax on line[index_max]
"""

