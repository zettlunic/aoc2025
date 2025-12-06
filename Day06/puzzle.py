import sys
import time
import re
from functools import reduce
import operator

filename = sys.argv[1] if len(sys.argv) > 1 else 'Day06/input.txt'
# filename = sys.argv[1] if len(sys.argv) > 1 else 'Day06/test.txt'

# Part 1

with open(filename) as file:
    lines = file.read().splitlines()

    split_lines = [l.split(' ') for l in lines]
    split_lines = [[inner for inner in l if inner != ''] for l in split_lines]
    y = len(split_lines)

    lines_with_numbers = [list(map(int, x)) for x in split_lines[:y - 1]]
    line_with_operators = split_lines[y - 1]

    x = len(line_with_operators)
    sum = 0
    for c in range(0, x):
        # grab first line's number
        acc = lines_with_numbers[0][c]
        for r in range(1, y - 1):
            if line_with_operators[c] == "+":
                acc += lines_with_numbers[r][c]
            else:
                acc *= lines_with_numbers[r][c]
        sum += acc

    print(sum)
            

# Part 2

with open(filename) as file:
    lines = file.read().splitlines()

    y = len(lines)

    o = [inner for inner in re.split(r"(?=[*+])", lines[y - 1]) if inner != '']
    operators_with_spacing = [i.removesuffix(' ') for i in o[:len(o) - 1]]
    operators_with_spacing.append(o[-1])
    print(operators_with_spacing)

    lines_with_numbers = [list(x) for x in lines[:y - 1]]
    print(lines_with_numbers)

    offset = 0
    sum = 0
    for opws in operators_with_spacing:
        cnums = len(opws)
        nums = []
        for c in range(offset, offset + cnums):
            num = ''
            for r in range(0, y - 1):
                num += lines_with_numbers[r][c]
            nums.append(num)

        offset += cnums + 1

        nums = list(map(int, nums))
        op = None

        if opws[0] == "+":
            op = operator.add
        else:
            op = operator.mul

        sum += reduce(op, nums)

    print(sum)