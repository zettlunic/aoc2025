import sys
import time

filename = sys.argv[1] if len(sys.argv) > 1 else 'Day03/input.txt'

# Part 1

# j=0
# with open(filename) as f:
#     for bank in f:
#         ints = list(map(int, bank.strip()))
#         pairs = [(int(ch), idx) for idx, ch in enumerate(bank.strip())]
#         s_pairs = sorted(pairs, key=lambda t: (-t[0], t[1]))
        
#         first = s_pairs[0][0]
#         first_idx = s_pairs[0][1]
#         second = -1
#         remainder=[]
#         if first_idx == len(ints) - 1:
#             # hit last. will be 2nd number.
#             remainder = ints[:len(ints)-1]
#             second = first
#             first = sorted(remainder, reverse=True)[0]
#         else:
#             remainder = ints[first_idx + 1:]
#             second = sorted(remainder, reverse=True)[0]

#         # print(f'jolts: {first}{second}')
#         j = j + (first * 10 + second)

# print(j)

# Part 2

sum=0
with open(filename) as f:
    for bank in f:
        j=''
        pairs = [(int(ch), idx) for idx, ch in enumerate(bank.strip())]
        s_pairs = sorted(pairs, key=lambda t: (-t[0], t[1]))

        count = 12

        while count > 0:
            for pair in s_pairs:
                highest = pair[0]
                highest_idx = pair[1]
                if len(bank.strip()) - highest_idx < count: #not enough numbers left
                        continue
                else: #found high number with enough space
                    j = j + f'{highest}'
                    count = count - 1
                    s_pairs.remove(pair)
                    s_pairs = [p for p in s_pairs if p[1] > highest_idx]
                    break

        # print(j)
        sum = sum + int(j)

print(sum)
