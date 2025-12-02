filename = 'Day01/input.txt'
# filename = 'Day01/test.txt'

# Part 1
with open(filename) as f:

    number = 50
    password = 0

    for line in map(str.strip, f):
        direction = line[0]
        value = int(line[1:])

        if direction == 'R':
            number = number + (value % 100)
        else:
            deduct = value % 100

            if deduct > number:
                number = number + 100 - deduct
            else:
                number = number - deduct
        
        number = number % 100

        if number == 0:
            password += 1

    print(password)

# -----------------------------------------------------------------

# Part 2
with open(filename) as f:

    number = 50
    password = 0

    for line in map(str.strip, f):
        direction = line[0]
        value = int(line[1:])

        if direction == "R":
            number = number + value
            if number >= 100:
                password += number // 100
        else:
            prev = number
            number = number - value
            if number <= 0:
                password += number // -100 + 1
                if prev == 0:
                    password -= 1
        
        number = number % 100

    print(password)

