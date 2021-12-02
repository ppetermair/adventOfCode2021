#!/usr/bin/env python3

from os import path

def main():
    increments = 0
    measurements = get_input()
    for index, measurement in enumerate(measurements):
        if index == 0:
            continue            
        elif int(measurements[index-1]) < int(measurement):
            increments+=1
    print("{} increments Part I".format(increments))

    increments = 0
    for index, measurement in enumerate(measurements):
        if index < 2:
            continue
        current_group = int(measurement) + int(measurements[index-1]) + int(measurements[index-2])
        previous_group = int(measurements[index-1]) + int(measurements[index-2]) + int(measurements[index-3])
        if previous_group < current_group:
            increments+=1
    print("{} increments Part II".format(increments))

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
