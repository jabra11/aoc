import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

start_pos = (0,0)

grid = data
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 'S':
            start_pos = (y,x)

def is_connected(grid, here, there):
    hy,hx = here
    y,x = there

    if (y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0])):
        return False

    if (data[y][x] == '.'):
        return False
    here = grid[hy][hx]

    ydif = hy-y
    xdif = hx-x

    above = ['|', 'L','J']
    below = ['|', '7','F']
    toright = ['-','7','J']
    toleft = ['-','F','L']


    match data[y][x]:
        case '|':
            if ydif == 1 and here in above:
                return True
            elif ydif == -1 and here in below:
                return True
        case '-':
            if xdif == 1 and here in toright:
                return True
            elif xdif == -1 and here in toleft:
                return True
        case 'L':
            if  ydif == -1 and here in below:
                return True
            elif xdif == 1 and here in toright:
                return True
        case 'J':
            if  ydif == -1 and here in below:
                return True
            elif xdif == -1 and here in toleft:
                return True
        case '7':
            if ydif == 1 and here in above:
                return True
            elif xdif == -1 and here in toleft:
                return True
        case 'F':
            if ydif == 1 and here in above:
                return True
            elif xdif == 1 and here in toright:
                return True
    return False



g = dict()
stack = list()
vis = list()

stack.append(start_pos)
sy,sx = start_pos
grid[sy] = grid[sy].replace('S', '-')

while len(stack)>0:
    hy,hx = stack[-1]
    cur = (hy,hx)
    stack.pop()
    vis.append(cur)


    for y in [-1,0,1]:
        for x in [-1,0,1]:
            if (y == 0 and x == y) or abs(y)+abs(x)>1:
                continue
            if (is_connected(grid, cur, (hy+y, hx+x))):
                if (hy+y,hx+x) in vis:
                    continue
                if cur in g:
                    g[cur].append((hy+y,hx+x))
                    if (hy+y,hx+x) in g:
                        g[(hy+y, hx+x)].append(cur)
                    else:
                        g[(hy+y, hx+x)] = [cur]
                else:
                    g[cur] = [(hy+y, hx+x)]
                    if (hy+y,hx+x) in g:
                        g[(hy+y, hx+x)].append(cur)
                    else:
                        g[(hy+y, hx+x)] = [cur]
                stack.append((hy+y, hx+x))

dis = dict()
for i in g.keys():
    dis[i] = 99999999
dis[start_pos] = 0

import queue
q = queue.Queue()
q.put(start_pos)
vis = [start_pos]

while not q.empty():
    cur = q.get()
    for i in g[cur]:
        dis[i] = min(dis[i], dis[cur]+1)
        if i not in vis:
            vis.append(i)
            q.put(i)
        
print(max(dis.values()))
