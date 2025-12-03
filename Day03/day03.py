import time

filename = 'Day03/input.txt'
# filename = 'Day03/test.txt'

# Part 1

start = time.perf_counter()

j=0
with open(filename) as f:
    for bank in f:
        ints = list(map(int, bank.strip()))
        pairs = [(int(ch), idx) for idx, ch in enumerate(bank.strip())]
        s_pairs = sorted(pairs, key=lambda t: (-t[0], t[1]))
        
        first = s_pairs[0][0]
        first_idx = s_pairs[0][1]
        second = -1
        remainder=[]
        if first_idx == len(ints) - 1:
            # hit last. will be 2nd number.
            remainder = ints[:len(ints)-1]
            second = first
            first = sorted(remainder, reverse=True)[0]
        else:
            remainder = ints[first_idx + 1:]
            second = sorted(remainder, reverse=True)[0]

        # print(f'jolts: {first}{second}')
        j = j + (first * 10 + second)

print(j)

elapsed_ms = (time.perf_counter() - start) * 1000
print(f"Part 1: {elapsed_ms:.2f} ms")

# Part 2

start = time.perf_counter()

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
                    s_pairs = sorted([pair for pair in pairs if pair[1] > highest_idx], key=lambda t: (-t[0], t[1]))
                    break

        # print(j)
        sum = sum + int(j)

print(sum)

# run your program logic
elapsed_ms = (time.perf_counter() - start) * 1000
print(f"Part 2: {elapsed_ms:.2f} ms")
