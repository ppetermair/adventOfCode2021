#!/usr/bin/env python3

from os import path

def main():
    horizontal = 0
    depth = 0
    depth_part2 = 0
    aim = 0

    for row in get_input():
        command = row.split(" ")[0]
        distance = int(row.split(" ")[1])
        if command == "forward":
            horizontal+=distance
            depth_part2+=aim*distance
        elif command == "up":
            depth-=distance
            aim-=distance
        elif command == "down":
            depth+=distance
            aim+=distance

    print("Part I horizontal {}, depth {}, multiplied {}".format(horizontal, depth, horizontal*depth))
    print("Part II horizontal {}, depth {}, multiplied {}".format(horizontal, depth_part2, horizontal*depth_part2))

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
