import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

xreg = 1
cycle = 0

answ=0

grid = list()
for i in range(6):
    grid.append(['.']*40)


def check_pix(cycle, xreg):
    cycle = cycle-1
    y = cycle // 40
    x = cycle % 40

    if xreg-1 <= x <= xreg+1:
        grid[y][x] = '#'

for i in data:
    match i.split(' '): 
        case a,b:
            for _ in range(2):
                cycle+=1
                check_pix(cycle, xreg)

            xreg += int(b)
        case a:
            cycle+=1
            check_pix(cycle, xreg)

for i in grid:
    for j in i:
        print(j,end='')
    print()
