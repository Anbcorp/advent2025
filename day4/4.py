#!/usr/bin/python3

import sys


def get_rolls_around(w, x, y, width, height):
    """
    -1,-1  0,-1 +1,-1
    -1, 0  0, 0 +1, 0
    -1,+1  0,+1 +1,+1
    """
    # print(f"Entering get_rolls_around for {x},{y}")
    adj_rolls = 0
    for ny in range(y - 1, y + 2):
        # edge or corner
        if ny < 0 or ny > height - 1:
            continue

        for nx in range(x - 1, x + 2):
            # edge or corner
            if nx < 0 or nx > width - 1:
                continue
            # 0,0
            if nx == x and ny == y:
                continue

            try:
                if w[ny][nx] == "@":
                    adj_rolls += 1
            except IndexError as e:
                print(f"IndexError at {nx},{ny}")
                raise e

    return adj_rolls


def solve_p1(w):
    return solve(w, False)


def solve_p2(w):
    moved_rolls = 0
    total_moved = 0
    print(w)
    moved_rolls = solve(w, True)
    total_moved += moved_rolls
    while moved_rolls > 0:
        print(w)
        moved_rolls = solve(w, True)
        total_moved += moved_rolls

    return total_moved


def solve(w, delete_roll=False):
    width = len(w[0])
    height = len(w)
    movable_rolls = 0
    print(f"warehouse is {width}x{height}")

    for y in range(0, height):
        for x in range(0, width):
            p = w[y][x]
            if p == "@":
                adj_rolls = get_rolls_around(w, x, y, width, height)
                if adj_rolls < 4:
                    print(f"{x},{y} can be moved, {adj_rolls} adjacent rolls")
                    movable_rolls += 1
                    if delete_roll:
                        w[y][x] = "."
    return movable_rolls


if __name__ == "__main__":
    fname = sys.argv[1]
    with open(fname, "r") as input:
        lines = [l.strip() for l in input.readlines()]
        w = [c for c in [list(l) for l in lines]]

    movable_rolls = solve_p2(w)
    print(f"{movable_rolls} can be moved")
