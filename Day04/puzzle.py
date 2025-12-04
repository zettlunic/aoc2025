import sys
import time

filename = sys.argv[1] if len(sys.argv) > 1 else 'Day04/input.txt'
# filename = sys.argv[1] if len(sys.argv) > 1 else 'Day04/test.txt'

# 4-directional (up, down, left, right)
DIR4 = [(1, 0), (-1, 0), (0, 1), (0, -1)]

# 8-directional (including diagonals)
DIR8 = DIR4 + [(1, 1), (1, -1), (-1, 1), (-1, -1)]

def neighbors4(r, c, rows, cols):
    for dr, dc in DIR4:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

def neighbors8(r, c, rows, cols):
    for dr, dc in DIR8:
        nr, nc = r + dr, c + dc
        if 0 <= nr < rows and 0 <= nc < cols:
            yield nr, nc

# Part 1

x=0

with open(filename) as file:
    grid = [list(line) for line in file.read().splitlines()]
    rows = len(grid)
    cols = len(grid[0])

    for r in range(rows):
        for c in range(cols):
            cell = grid[r][c]
            if cell != "@": continue
            # print(r, c, cell)

            n = neighbors8(r, c, rows, cols)
            
            i=0
            for nr, nc in n:
                if grid[nr][nc] == "@":
                    i += 1
                    if i > 3: break
            if i < 4:
                # print(f'found on {r},{c}')
                x += 1

print(x)

# Part 2

x=0

with open(filename) as file:
    grid = [list(line) for line in file.read().splitlines()]
    rows = len(grid)
    cols = len(grid[0])
    
    while True:
        could_remove=False
        for r in range(rows):
            for c in range(cols):
                cell = grid[r][c]
                if cell != "@": continue
                # print(r, c, cell)

                n = neighbors8(r, c, rows, cols)
                
                i=0
                for nr, nc in n:
                    if grid[nr][nc] == "@":
                        i += 1
                        if i > 3: break
                if i < 4:
                    # print(f'removing from {r},{c}')
                    grid[r][c] = "."
                    could_remove=True
                    x += 1
        if could_remove == False: break

print(x)
