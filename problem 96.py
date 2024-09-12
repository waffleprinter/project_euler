def is_valid(grid, r, c, v): # ROW, COLUMN, VALUE
    not_in_row = v not in grid[r]
    not_in_col = v not in [grid[i][c] for i in range(9)]

    square = [grid[i][j] for i in range(r // 3 * 3, r // 3 * 3 + 3) for j in range(c // 3 * 3, c // 3 * 3 + 3)]
    not_in_square = v not in square

    return not_in_row and not_in_col and not_in_square


def solve(grid, r=0, c=0):
    if r == 9:
        return True

    if c == 9:
        return solve(grid, r + 1, 0)

    if grid[r][c] != 0:
        return solve(grid, r, c + 1)

    for v in range(1, 10):
        if is_valid(grid, r, c, v):
            grid[r][c] = v

            if solve(grid, r, c + 1):
                return True

            grid[r][c] = 0

    return False


with open("problem96grids", "r") as f:
    string = f.readlines() # INITIALIZE
    string = [i.replace("\n", "") for i in string] # GET RID OF NEWLINE CHARACTERS
    string = [string[i] for i in range(len(string)) if i % 10 != 0] # GET RID OF "GRID X" STRINGS
    string = [[int(i) for i in c] for c in string] # SEPARATE 'xxxxxxxxx' INTO ROWS

    grids = []

    for i in range(0, len(string), 9):
        grid = []

        for j in range(9):
            grid.append(string[i + j])

        grids.append(grid)


ans = 0

for grid in grids:
    solve(grid, 0, 0)
    ans += int(str(grid[0][0]) + str(grid[0][1]) + str(grid[0][2]))

print(ans)
