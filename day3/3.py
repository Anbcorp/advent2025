#!/usr/bin/env python3

import copy
import sys

"""
P2
form highest n digits number from a l length line
create a n-length list ans
will receiver numbers we should keep
iteration n [None, None, 8, None, 3]
iteration n + x [None, 3, 8, None, 3]
final -> 383

At all step we must be able to convert relative indexes to absolute

find maxi, verify there is >=n-1 digits after to form the n digits answer
yes
    we know the rest of the answer starts with this digit
    if len(line[maxi+i:])+iterations == n
        there is just enough remaining digits to fill the answer
        append all remaining digits and exit
    else:
        all the previous digits are excluded
        continue with line[maxi+1:] and n-1, keep track of the starting index relative to the full line
no
    the digit must keep it relative index in the final number
    put line[maxi] in ans[maxi]
    continue with line and n-1 (reset the relative position)

This cannot keep track of what to keep
two lists, for a 2 digit answer
    line = [1,2,3,4]
    res = [None, None, None, None]

    Step1 :
        l = [1,2,3,None]
        r = [None,None,None,4]

    Step2:
        l = [1.2.None,None]
        r = [None,None,3,4]
    len([ v for v in r if l]) == 2 => Final step
    Answer is 34

"""
def nlen(seq):
    return len([ v for v in seq if v])

def nmax(seq):
    #print(f"NMAX {seq} - {len(seq)}")
    return max([ v for v in seq if v])

def find_answer(line):
    """ not 42 """
    in_line = list(line)
    out_line = [None]*len(line)
    print(f"START: {in_line}\n       {out_line}")
    relpos = 0
    prevpos = 0
    while nlen(out_line) < 12:
        m = nmax(in_line[relpos:])
        mi = in_line[relpos:].index(m)+relpos
        print(f"max is {m}@{mi}")
        if nlen(in_line[mi:]) == 12 - nlen(out_line):
            print(f"FINAL - copy all from {mi} to {len(in_line[mi:])+1}")
            # insert all remaining in out_line
            for i in range(mi,len(in_line[mi:])+mi):
                if in_line[i]:
                    out_line[i] = in_line[i]
                    in_line[i] = None
            print(f"{in_line}\n{out_line}")
            break

        print(f"{nlen(in_line[mi:])} > 12 - {nlen(out_line)}")
        # We use len here because some digits may already be gone
        if len(in_line[mi:]) > 12 - nlen(out_line):
            print("RESANDMOVE")
            in_line[mi] = None
            out_line[mi] = m
            # digits before mi are lower and there are enough 
            # digits behind to form the answer
            # continue using the remaining digits
            prevpos=relpos
            relpos=mi+1
            print(f"{in_line}\n{out_line}")
            continue
        else:
            relpos=prevpos
            print(f"RESANDBACK to {relpos}")
            # there is not enough digits left after mi
            in_line[mi] = None
            out_line[mi] = m
            # reset relpos to find the next max digit in all in_line
            print(f"{in_line}\n{out_line}")

    return [v for v in out_line if v]


def get_next_digit(seq, res_len, rel_pos):
    m = max(seq)
    mi = seq.index(m)
    print(f"  max is {m} at {mi}")
    # Special where we have to keep all remaining digits
    if len(seq[mi:]) == res_len:
        return seq[mi:]

    if len(seq[mi:]) > res_len:
        # Keep it as first digit, we will find other in the rest of the seq
        get_next_digit(seq[mi+1:], res_len-1, mi)

    else:
        # we cannot find all remaining digits in the remaining seq
        # Keep it and start again
        pass # this is goind nowhere

def part1(fname):
    total = 0
    for line in input.readlines():
        i = []
        line = line.strip()
        print(f"line is {line}")
        m = max(line)
        mi = line.index(m)
        print(f"  max is {m} at {mi}")
        i.append(mi)
        # Need 12 digits so if m is after [:-12] if needs to stay there
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


fname = sys.argv[1]
with open(fname, 'r') as input:
    total = 0
    for line in input.readlines():
        res = find_answer(line.strip())
        ires = int(''.join(res))
        print(f"{ires} - {len(res)}")
        total += ires
    print(f"TOTAL: {total}")
