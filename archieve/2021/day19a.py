import sys; datafilepath = sys.argv[1]
raw_data = open(datafilepath).read().splitlines()

import math

scanners = list()
tmp = list()

for i in raw_data:
    if len(i) == 0:
        scanners.append(tmp.copy())
        tmp.clear()
    elif i[0:2] == '--':
        continue
    else:
        (a,b,c) = i.split(',')
        tmp.append((int(a), int(b), int(c)))
scanners.append(tmp.copy())

graphs = list()
#overlaps = list()

for scanner in scanners:
    g = dict()
    for i in range(len(scanner)):
        g[scanner[i]] = list()
        for j in range(len(scanner)):
            x1,y1,z1 = scanner[i]
            x2,y2,z2 = scanner[j]
            dx,dy,dz = abs(x1-x2), abs(y1-y2),abs(z1-z2)

            dis = round(math.sqrt(dx**2+dy**2+dz**2),6)
            g[scanner[i]].append((scanner[j], dis))
    graphs.append(g.copy())

overlaps = list()
for i in range(len(scanners)):
    tmp = list()
    for j in range(len(scanners)):
        tmp.append(list())
    overlaps.append(tmp.copy())

for i in range(len(graphs[0:])):
    g1 = graphs[i]
    for j in range(i+1, len(graphs)):
        g2 = graphs[j]

        for g1node in g1.keys():
            s1 = set([x for _,x in g1[g1node]])

            for g2node in g2.keys():
                s2 = set([ x for _,x in g2[g2node] ])
                if len(s1 & s2) >= 12:
                    overlaps[i][j].append((g1node,g2node))
                    overlaps[j][i].append((g2node,g1node))

scanner_configs = list(list())
for i in range(len(scanners)):
    tmp = list()
    for j in range(len(scanners)):
        tmp.append(None)
    scanner_configs.append(tmp.copy())

for i in range(len(scanners)):
    for j in range(len(scanners)):
        for l in range(0,2):
            use_i = i
            use_j = j

            if l%2 == 0:
                use_i = j
                use_j = i


            config = dict()
            xfactor = 1
            yfactor = 1
            zfactor = 1
            axis_map = [0,1,2]

            good = True
            for x in range(0,6):
                for y in range(0,6):
                    for z in range(0,6):
                        good = True
                        if x % 2 == 0:
                            xfactor = 1
                        else:
                            xfactor = -1
                        if y % 2 == 0:
                            yfactor = 1
                        else:
                            yfactor = -1
                        if z % 2 == 0:
                            zfactor = 1
                        else:
                            zfactor = -1
                        axis_map[0] = x%3
                        axis_map[1] = (y+1)%3
                        axis_map[2] = (z+2)%3

                        if len(overlaps[i][j]) == 0:
                            continue

                        src, imag = overlaps[i][j][0]
                        if l%2 == 0:
                            tmp = src
                            src = imag
                            imag = tmp

                        xoffs = src[0] - (xfactor * imag[axis_map[0]])
                        yoffs = src[1] - (yfactor * imag[axis_map[1]])
                        zoffs = src[2] - (zfactor * imag[axis_map[2]])

                        for k in range(1,len(overlaps[use_i][use_j])):
                            src, imag = overlaps[use_i][use_j][k]

                            if l%2 == 0:
                                tmp = src
                                src = imag
                                imag = tmp

                            res = (src[0] - (xfactor * imag[axis_map[0]]) == xoffs,
                                   src[1] - (yfactor * imag[axis_map[1]]) == yoffs,
                                   src[2] - (zfactor * imag[axis_map[2]]) == zoffs)

                            if res != (True, True, True):
                                good = False

                        if good:
                            scanner_configs[use_i][use_j] = ((xoffs,yoffs,zoffs),
                                    ((axis_map[0],xfactor), (axis_map[1],yfactor),
                                    (axis_map[2],zfactor)))
                            break
                    if good: 
                        break
                if good:
                    break


graph = dict()
for i in range(len(scanners)):
    graph[i] = list()

for i in range(len(scanners)):
    for j in range(i+1,len(scanners)):
        if scanner_configs[i][j] != None:
            #print(i,j,scanner_configs[i][j])
            graph[i].append(j)
        if scanner_configs[j][i] != None:
            #print(j,i,scanner_configs[j][i])
            graph[j].append(i)

# find paths from each scanner to scanner 0
paths = list(list())
import queue
paths.append(list())
for i in range(1,len(scanners)):
    dis = list()
    pred = list()
    for _ in range(len(scanners)):
        dis.append(99999999999)
        pred.append(None)

    dis[i] = 0
    q = queue.Queue()
    q.put((i,None))

    while not q.empty():
        cur,par = q.get()
        if par != None and dis[cur] > dis[par] + 1:
            dis[cur] = dis[par] + 1
            pred[cur] = par

        if cur == 0:
            break

        for j in graph[cur]:
            q.put((j,cur))
    
    paths.append(list())
    cur = 0
    while cur != None:
        paths[i].append(cur)
        cur = pred[cur]
    paths[i] = list(reversed(paths[i]))


cubic_sets = list()
for scanner in scanners:
    tmp = set()
    for j in scanner:
        tmp.add(j)
    cubic_sets.append(tmp.copy())


for i in range(1,len(scanners)):
    fro = paths[i][0]
    for to in paths[i][1:]:
        tform = scanner_configs[to][fro]
        for point in scanners[fro]:
            x = tform[0][0] + point[tform[1][0][0]] * tform[1][0][1]
            y = tform[0][1] + point[tform[1][1][0]] * tform[1][1][1]
            z = tform[0][2] + point[tform[1][2][0]] * tform[1][2][1]
            scanners[to].append((x,y,z))

        fro = to

print(len(set(scanners[0])))
