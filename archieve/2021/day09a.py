hmap = [ list(x) for x in open('etc/in').read().splitlines() ]

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
res = 0
for i,j in low_points:
    res += 1+hmap[i][j]
print(res)
