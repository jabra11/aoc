def main():
    grid = open("data.txt").readlines()

    for i in range(0, len(grid)):
        grid[i] = grid[i][:-1]

    x_width = len(grid[i])
    y_length = len(grid)

    ctr = 0
    y_pos = 0
    x_pos = 0
    product = 1

    for i in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
        while y_pos < y_length:
            if grid[y_pos][x_pos % x_width] == '#':
                ctr += 1

            x_pos += i[0]
            y_pos += i[1]

        print(ctr)
        product *= ctr
        
        x_pos=0
        y_pos=0
        ctr=0

    print(product)

main()
