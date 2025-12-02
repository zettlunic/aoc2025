filename = 'Day02/input.txt'
# filename = 'Day02/test.txt'

# Part 1
with open(filename) as f:
    ranges=f.read().strip().split(',')

    result = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        nums = [str(n) for n in range(start, end + 1)]

        for x in nums:
            count = len(x)

            if count % 2 == 0:
                n = count // 2
                chunks = [x[i:i+n] for i in range(0, len(x), n)]
                #print(chunks)

                if len(set(chunks)) <= 1:
                        # print(f'Found matching number: {x}')
                        result = result + int(x)

    print(result)

# Part 2
with open(filename) as f:
    ranges=f.read().strip().split(',')

    result = 0

    for r in ranges:
        start, end = map(int, r.split('-'))
        nums = [str(n) for n in range(start, end + 1)]

        for x in nums:
            count = len(x)

            for i in range(0, count // 2):
                part = x[0:i + 1]
                # print(f'{part}, length: {len(part)}')

                n = len(part)
                chunks = [x[i:i+n] for i in range(0, len(x), n)]
                #print(chunks)
                if len(set(chunks)) <= 1:
                    #print(f'Found matching number: {x}')
                    result = result + int(x)
                    break

    print(result)