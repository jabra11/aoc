def solve():
    print(5)


def calc_new_grid(grid):
    ans = grid.copy()

    for i in range(len(grid)):
        for j in range(len(grid[i])):


            if grid[i][j] == '.':
                ans[i] = ans[i][0:j] + '.' + ans[i][j+1:]
                continue

            print('starting {}/{}'.format(j,i))

            ctr = 0

            # check left 
            x = j-1
            y = i
            while x >= 0: 
                if grid[y][x] == '#': 
                    ctr+=1
                    print('l')
                    break
                if grid[y][x] == 'L': 
                    break
                x -= 1
            # check right
            x = j+1
            y = i
            while x < len(grid[i]): 
                if grid[y][x] == '#': 
                    ctr+=1
                    print('r')
                    break
                if grid[y][x] == 'L': 
                    break
                x += 1

            # check top
            x = j
            y = i-1
            while y >= 0:
                if grid[y][x] == '#':
                    ctr+=1
                    print('t')
                    break
                if grid[y][x] == 'L': 
                    break
                y-=1

            # check bottom
            x = j
            y = i+1
            while y < len(grid):
                if grid[y][x] == '#':
                    ctr+=1
                    print('b')
                    break
                if grid[y][x] == 'L': 
                    break
                y+=1

            # check left top
            x = j-1
            y = i-1
            while (y >= 0 and x >= 0):
                if grid[y][x] == '#':
                    ctr+=1
                    print('lt')
                    break
                if grid[y][x] == 'L': 
                    break
                y-=1
                x-=1

            # check left bottom
            x = j-1
            y = i+1
            while (y < len(grid) and x >= 0):
                if grid[y][x] == '#':
                    ctr+=1
                    print('lb')
                    break
                if grid[y][x] == 'L': 
                    break
                y+=1
                x-=1

            # check right bottom
            x = j+1
            y = i+1
            while (y < len(grid) and x < len(grid[i])):
                if grid[y][x] == '#':
                    ctr+=1
                    print('rb')
                    break
                if grid[y][x] == 'L': 
                    break
                y+=1
                x+=1

            # check right top
            x = j+1
            y = i-1
            while (y >= 0 and x < len(grid[i])):
                if grid[y][x] == '#':
                    print('rt')
                    ctr+=1
                    break
                if grid[y][x] == 'L': 
                    break
                y-=1
                x+=1
            
            print("ctr: {}".format(ctr))

            if ctr >= 5:
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
