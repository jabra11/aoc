grid = [ list(x) for x in open('etc/in').read().splitlines() ]
inf = 99999999999
for i in range(len(grid)):
    grid[i] = [inf] + [int(x) for x in grid[i]] + [inf]
grid.insert(0,[inf]*len(grid[0]))
grid.insert(len(grid),[inf]*len(grid[0]))

ctr=0
for step in range(0,100):
    flashers = list()
    for i in range(1,len(grid)-1):
        for j in range(1,len(grid[i])-1):
            grid[i][j] += 1
            if grid[i][j]>9:
                flashers.append((i,j))

    flashed = set()
    while not len(flashers)==0:
        i,j = flashers[len(flashers)-1]
        flashers.pop()

        if (i,j) in flashed or grid[i][j] >= inf:
            continue
        flashed.add((i,j))
        ctr+=1

        for k in range(0,3):
            grid[i-1][j-1+k] += 1
            if grid[i-1][j-1+k] > 9:
                flashers.append((i-1,j-1+k))

        for k in range(0,3):
            grid[i+1][j-1+k] += 1
            if grid[i+1][j-1+k] > 9:
                flashers.append((i+1,j-1+k))

        grid[i][j-1] += 1
        if grid[i][j-1] > 9:
            flashers.append((i,j-1))

        grid[i][j+1] += 1
        if grid[i][j+1] > 9:
            flashers.append((i,j+1))
    
    for i,j in flashed:
        grid[i][j] = 0

print(ctr)
