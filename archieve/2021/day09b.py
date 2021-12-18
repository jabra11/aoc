import sys; datafilepath = sys.argv[1]
hmap = [ list(x) for x in open(datafilepath).read().splitlines() ]

inf = 99

for i in range(len(hmap)):
    hmap[i] = [inf] + [int(x) for x in hmap[i]] + [inf]

hmap.insert(0,[inf]*len(hmap[0]))
hmap.insert(len(hmap),[inf]*len(hmap[0]))

low_points=list()

for i in range(1,len(hmap)-1):
    for j in range(1,len(hmap[i])-1):
        cur = hmap[i][j]
        ctr=0
        if hmap[i][j-1] <= cur:
            ctr+=1
        if hmap[i][j+1] <= cur:
            ctr+=1
        if hmap[i-1][j] <= cur:
            ctr+=1
        if hmap[i+1][j] <= cur:
            ctr+=1
        if ctr == 0:
            low_points.append((i,j))

# find basins
import queue

basins = list(set())

for (i,j) in low_points:
    s = set()
    q = queue.Queue()
    q.put((i,j))
    while not q.empty():
        y,x = q.get()
        if (y,x) in s or hmap[y][x] >= 9:
            continue
        s.add((y,x))
        q.put((y,x-1))
        q.put((y,x+1))
        q.put((y+1,x))
        q.put((y-1,x))
    basins.append(s)

sizes = [ len(s) for s in basins ]
sizes = sorted(sizes)
ans = 1
for i in range(3):
    ans *= sizes[len(sizes)-1-i]
print(ans)
