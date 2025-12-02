#!/usr/bin/env python3

"""# Day 1

L -
R +

11 -> R8 -> 19 -> L19 -> 0

0 -> L1 -> 99
99 -> R1 -> 0
Modulo ??


Starts at 50


Make all rotations
Count when the result is 0
"""


def decode(ins):
    direction = ins[0]
    count = int(ins[1:])

    if direction == 'R':
        mult = 1
    else:
        mult = -1
    print(f"{direction} {count} -> {mult*count}")
    return mult*count


with open("1_input", 'r') as input:
    dial = 50
    result = 0
    click=0
    for line in input.readlines():
        noclick=0
        if dial == 0:
            noclick=1
        dial += decode(line.strip())
        if dial < 0:
            while dial < 0:
                if noclick == 0:
                    click += 1
                    print("click")
                else:
                    noclick=0
                dial = 100+dial
        elif dial > 99:
            while dial > 99:
                # Extra click in this case
                if dial != 100 and noclick == 0:
                    click += 1
                    print("click")
                elif noclick==1:
                    print("will click")
                    noclick=0
                dial = dial-100
                print(f"dial is {dial}")
        if dial == 0:
            result +=1
        print(f"Dial {dial}")
    print(f"Password: {result}+{click} -> {result+click}")
    # Between 5785 and 6250
