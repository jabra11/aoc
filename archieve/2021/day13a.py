import sys; datafilepath = sys.argv[1]
data = [x for x in open(datafilepath).read().split('\n\n')]

points = [ x.split(',') for x in data[0].splitlines()]
for i in range(len(points)):
    a,b = points[i]
    points[i] = [int(a), int(b)]

folds = list()
for i in data[1].splitlines():
    if 'x' in i:
        folds.append(['x', int(i[13:])])
    else:
        folds.append(['y', int(i[13:])])

grid = list(list())

min_x = min([x for x,_ in points])
min_y = min([y for _,y in points])
max_x = max([x for x,_ in points])
max_y = max([y for _,y in points])

for i in range(min_y,max_y+1):
    grid.append([0] * (max_x-min_x+1))

for (x,y) in points:
    grid[y-min_y][x-min_x] = 1

for (coord, idx) in folds[0:1]:
    if coord == 'y':
        tmp = grid[0:idx].copy()

        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                if tmp[i][j] == 0:
                    tmp[i][j] = grid[len(grid)-1-i][j]
        grid = tmp
    else:
        tmp = list(list())
        for i in range(len(grid)):
            tmp.append(grid[i][0:idx].copy())

        for i in range(len(tmp)):
            for j in range(len(tmp[i])):
                if tmp[i][j] == 0:
                    tmp[i][j] = grid[i][len(grid[i])-j-1]
        grid = tmp

ctr=0
for i in grid:
    for j in i:
        if j == 1:
            ctr+=1
print(ctr)
