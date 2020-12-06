def main():
    grid = open("data.txt").readlines()

    for i in range(0, len(grid)):
        grid[i] = grid[i][:-1]

    x_width = len(grid[i])
    y_length = len(grid)

    ctr = 0
    y_pos = 0
    x_pos = 0

    while y_pos < y_length:
        if grid[y_pos][x_pos % x_width] == '#':
            ctr += 1

        x_pos += 3
        y_pos += 1

    print(ctr)

main()
