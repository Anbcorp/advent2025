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
    clicks=0
    for line in input.readlines():
        # Compute distance to 0
        # if turns > distance, there is at least one click to 0 (depend of the direction we turn !!)
        # 1. calculate number of full turns
        # 2. Use remainder
        # 2a. If land on 0 -> nothing (account for in the result)
        # 2b. If > 0, add one click.
        positiveDistance = (100 - dial)%100
        negativeDistance = dial

        print(f"+distance {positiveDistance} -distance {negativeDistance}")

        turns = decode(line.strip())
        # R side
        if turns > 0:
            clicks += turns//100 
            if positiveDistance > 0 and turns%100 > positiveDistance:
               clicks += 1
        # L side
        if turns < 0:
            clicks += abs(turns)//100
            if negativeDistance > 0 and abs(turns)%100 > negativeDistance:
                clicks += 1

        dial += turns
        dial = dial%100

        if dial == 0:
            result +=1
        print(f"Dial {dial}, clicks to zero {clicks}")
    print(f"Password: {result}+{clicks} -> {result+clicks}")
    # Between 5785 and 6250
