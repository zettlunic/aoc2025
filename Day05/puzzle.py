import sys
import time

filename = sys.argv[1] if len(sys.argv) > 1 else 'Day05/input.txt'
# filename = sys.argv[1] if len(sys.argv) > 1 else 'Day05/test.txt'

# Part 1

x=0

with open(filename) as file:
    lines = file.read().splitlines()
    split_idx = lines.index('')
    ranges = [tuple(map(int, r.split('-'))) for r in lines[:split_idx]]
    ids = list(map(int, lines[split_idx + 1:]))

    for id in ids:
        included=False
        for range_tuple in ranges:
            if id in range(range_tuple[0], range_tuple[1]+1):
                included=True
                # print(f'{id} is in {range_tuple}')
                break
        if included:
            x += 1

print(x)

# Part 2

with open(filename) as file:
    lines = file.read().splitlines()
    split_idx = lines.index('')
    ranges = [tuple(map(int, r.split('-'))) for r in lines[:split_idx]]
    ranges = sorted(ranges, key=lambda t: t[0])

    valid_ranges = [ranges[0]]
    for r in ranges[1:]:

        found=False
        for (p_idx, p_valid) in enumerate(valid_ranges):
            if r[0] in range(p_valid[0], p_valid[1] + 1):
                found=True
                if r[1] > p_valid[1]:
                    # update upper bounds
                    valid_ranges = valid_ranges[:p_idx]
                    valid_ranges.append((p_valid[0], r[1]))
                # else:
                    #swallow
        
        if not found:
            valid_ranges.append(r)
        
        # print(valid_ranges)

    sum=0
    for r in valid_ranges:
        sum += len(range(r[0], r[1]+1))
    print(sum)
