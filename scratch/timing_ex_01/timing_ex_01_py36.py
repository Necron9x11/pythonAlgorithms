#!/usr/bin/env python3
#
# Python Algorithms
# Chapter 1 Timing Example
# pp.3-4
#
# Author: Daniel Raphael
#
# ---------------------------------------------------------------------------------------------------------------------
#
# This program draws on the books opening discussion about algorithm efficiency and program execution time.
# I have taken the example and expanded it to include code to track execution timing using the time module.
#
#
# ---------------------------------------------------------------------------------------------------------------------

import time
import argparse

# Setup Argument Parser
#
parser = argparse.ArgumentParser('is a test program that measures the execution time of several different List '
                                 'operations. The amount of data processed by the list, and thus the overall total '
                                 'execution time, can be controlled via commandline options. List operations.')
parser.add_argument('-d', '--debug', action="store_true", help='Turns on additional debugging output to std in.'
                                                               'if available')
parser.add_argument('count', nargs="?", default=100000, type=int,
                    help='the count parameter passes a number representing the number of items each list should'
                         'be composed of')
args = parser.parse_args()

# --------------------------

# Not in the Book

time_01_start = time.time()

count = args.count

nums01 = [x for x in range(count)]

time_01_stop = time.time()

runtime_01 = time_01_stop - time_01_start

print('\nMethod 1 (List Comprehension) runtime: ')
print(f'Start: {time_01_start} Stop: {time_01_stop} Run Length: {runtime_01}')

# --------------------------

# In the book

time_02_start = time.time()

nums02 = []

for x in range(count):
    nums02.append(x)

nums01.reverse()

time_02_stop = time.time()

runtime_02 = time_02_stop - time_02_start

print('\nMethod 2 (For Loop with List .append Method) runtime: ')
print(f'Start: {time_02_start} Stop: {time_02_stop} Run Length: {runtime_02}')

# --------------------------

# In the Book

time_03_start = time.time()

nums03 = []

for x in range(count):
    nums03.insert(0, x)

time_03_stop = time.time()

runtime_03 = time_03_stop - time_03_start

print('\nMethod 3 (For Loop with List .insert Method to insert at List Beginning) runtime: ')
print(f'Start: {time_03_start} Stop: {time_03_stop} Run Length: {runtime_03}')

total_runtime = time_03_stop - time_01_start
print('\n')
print('-' * 80)
print('\nTotal Program runtime: ')
print(f'Start: {time_01_start} Stop: {time_03_stop} Run Length: {total_runtime}')
