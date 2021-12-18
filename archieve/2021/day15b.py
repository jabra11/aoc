import sys; datafilepath = sys.argv[1]
grid = [ list(map (int, x)) for x in open(datafilepath).read().splitlines() ]

for i in range(len(grid)):
    tmp = list()
    for j in range(0,5):
        for k in grid[i]:
            tmp.append(k+j)
    grid[i] = tmp

tmp = list()
for j in range(0,5):
    for y in range(len(grid)):
        tmptmp=list()
        for k in grid[y]:
            if k+j <= 9:
                tmptmp.append(k+j)
            else:
                tmptmp.append(k+j-9)
        tmp.append(tmptmp)
grid = tmp

inf = 999999999999

start_pos = (0,0)
end_pos = (len(grid)-1,len(grid)-1)

g = dict()

for i in range(0,len(grid)):
    for j in range(0,len(grid)):
        g[(i,j)] = list()
        if i > 0:
            g[(i,j)].append((i-1,j))
        if i < len(grid)-1:
            g[(i,j)].append((i+1,j))
        if j > 0:
            g[(i,j)].append((i,j-1))
        if j < len(grid)-1:
            g[(i,j)].append((i,j+1))

riskm = dict()
for i in range(len(grid)):
    for j in range(len(grid)):
        riskm[(i,j)] = inf
riskm[(0,0)] = 0

import queue
vis = set()
q = queue.PriorityQueue()
q.put((0, start_pos))

while not q.empty():
    cur = q.get()[1]
    for i in g[cur]:
        if i not in vis:
            riskm[i] = riskm[cur] + grid[i[0]][i[1]]
            vis.add(i)
            q.put((riskm[i], i))
        else:
            if riskm[cur] + grid[i[0]][i[1]] < riskm[i]:
                riskm[i] = riskm[cur] + grid[i[0]][i[1]]

print(riskm[end_pos])
