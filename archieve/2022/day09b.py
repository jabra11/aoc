import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()
import math

l = 10

hpos=[(0,0)] * l
vis = set()
vis.add(hpos[l-1])

def sim_mv(head,tail):
    hx,hy = hpos[head]
    tx,ty = hpos[tail]

    dis = math.sqrt(abs(hx-tx)+abs(hy-ty))

    if dis > 1:
        if hx == tx or hy == ty:
            if hx == tx:
                if hy > ty:
                    ty += 1
                else:
                    ty -= 1
            else:
                if hx > tx:
                    tx += 1
                else:
                    tx -= 1
        else:
            if dis > 1.5:
                if hx > tx and hy > ty:
                    tx += 1
                    ty += 1
                elif hx > tx and hy < ty:
                    tx += 1
                    ty -= 1
                elif hx < tx and hy > ty:
                    tx -= 1
                    ty += 1
                else:
                    ty -= 1
                    tx -= 1
    hpos[tail] = tx,ty


for ins in data:
    d,n = ins.split(' ')
    n = int(n)
    for _ in range(n):
        x,y = hpos[0]    
        match d:
            case 'U':
                hpos[0] = x,y+1
            case 'D':
                hpos[0] = x,y-1
            case 'L':
                hpos[0] = x-1,y
            case 'R':
                hpos[0] = x+1,y

        for j in range(1,len(hpos)):
            sim_mv(j-1,j) 
            if  j == l-1:
                vis.add(hpos[j])

print(len(vis))
