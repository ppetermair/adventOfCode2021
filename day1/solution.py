#!/usr/bin/env python3

from os import path

def main():
    increments = 0
    measurements = get_input()
    for index, measurement in enumerate(measurements):
        #print("{} reading: {}".format(index, measurement))
        if index == 0:
            print("{} (N/A - no previous measurement)".format(measurement))            
        elif int(measurements[index-1]) < int(measurement):
            print("{} {}".format(measurement, "(increased)"))
            increments+=1
        else:
            print("{} {}".format(measurement, "(decreased)"))
    print("{} increments".format(increments))

def get_input():
    with open(path.join(path.dirname(__file__), 'input')) as f:
        return [i.strip() for i in f.readlines()]

if __name__ == '__main__':
    main()
