def solve():
    print(5)


def calc_new_grid(grid):
    ans = grid.copy()

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '.':
                ans[i] = ans[i][0:j] + '.' + ans[i][j+1:]
                continue

            ctr = 0
            if ((i > 0 and i < len(grid)-1) and (j > 0 and j < len(grid[i])-1)):
                if grid[i-1][j-1] == '#': ctr +=1
                if grid[i-1][j] == '#': ctr +=1
                if grid[i-1][j+1] == '#': ctr +=1
                if grid[i][j-1] == '#': ctr +=1
                if grid[i][j+1] == '#': ctr +=1
                if grid[i+1][j-1] == '#': ctr +=1
                if grid[i+1][j] == '#': ctr +=1
                if grid[i+1][j+1] == '#': ctr +=1
            else:
                if i == 0 and j == 0:
                    if grid[0][1] == '#': ctr+=1
                    if grid[1][0] == '#': ctr+=1
                    if grid[1][1] == '#': ctr+=1

                elif (i == len(grid)-1 and j == 0):
                    if grid[i-1][j] == '#': ctr+=1
                    if grid[i-1][j+1] == '#': ctr+=1
                    if grid[i][j+1] == '#': ctr+=1

                elif (i == 0 and j == len(grid[i])-1):
                    if grid[i][j-1] == '#': ctr+=1
                    if grid[i+1][j] == '#': ctr+=1
                    if grid[i+1][j-1] == '#': ctr+=1

                elif (i == len(grid)-1 and j == len(grid[i])-1):
                    if grid[i][j-1] == '#': ctr+=1
                    if grid[i-1][j] == '#': ctr+=1
                    if grid[i-1][j-1] == '#': ctr+=1

                else:
                    if i == 0:
                        if grid[i][j-1] == '#': ctr+=1
                        if grid[i][j+1] == '#': ctr+=1
                        if grid[i+1][j+1] == '#': ctr+=1
                        if grid[i+1][j] == '#': ctr+=1
                        if grid[i+1][j-1] == '#': ctr+=1
                    if i == len(grid)-1:
                        if grid[i][j-1] == '#': ctr+=1
                        if grid[i][j+1] == '#': ctr+=1
                        if grid[i-1][j+1] == '#': ctr+=1
                        if grid[i-1][j] == '#': ctr+=1
                        if grid[i-1][j-1] == '#': ctr+=1
                    if j == 0:
                        if grid[i+1][j] == '#': ctr+=1
                        if grid[i+1][j+1] == '#': ctr+=1
                        if grid[i][j+1] == '#': ctr+=1
                        if grid[i-1][j] == '#': ctr+=1
                        if grid[i-1][j+1] == '#': ctr+=1
                    if j == len(grid[i])-1:
                        if grid[i+1][j] == '#': ctr+=1
                        if grid[i+1][j-1] == '#': ctr+=1
                        if grid[i][j-1] == '#': ctr+=1
                        if grid[i-1][j] == '#': ctr+=1
                        if grid[i-1][j-1] == '#': ctr+=1


            if ctr >= 4:
                ans[i] = ans[i][0:j] + 'L' + ans[i][j+1:]
            elif (ctr == 0 and grid[i][j] == 'L'):
                ans[i] = ans[i][0:j] + '#' + ans[i][j+1:]
            

    return ans


def print_grid(grid):
    for i in grid:
        print(i)

    print('\n\n')

def main():
    grid = open('etc/data.txt').read().splitlines()

    last = grid.copy()
    ctr=0
    print_grid(last)
    while ctr < 1000:
        new_grid = calc_new_grid(last)
        if new_grid == last:
            break
        else:
            last = new_grid
            print_grid(last)
        ctr+=1

    ans = 0
    for i in last:
        for j in i:
            if j == '#':
                ans += 1 


    print(ans)


main()
