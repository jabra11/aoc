import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()
d = data

cnt=0

l=range(len(data))
h=range(len(data[0]))
ym=len(data)
xm=len(data[0])

cdts = [(y,x) for x in l for y in h]

def good(y,x):
    r=0
    for i in range(x+1,xm):
        r+=1
        if d[y][i] >= d[y][x]:
            break
    l=0
    for i in range(0,x):
        l+=1
        if d[y][x-i-1] >= d[y][x]:
            break
    u=0
    for i in range(0,y):
        u+=1
        if d[y-i-1][x] >= d[y][x]:
            break
    dd=0
    for i in range(y+1,ym):
        dd+=1
        if d[i][x] >= d[y][x]:
            break

    return r*l*u*dd

scores = [ good(x,y) for (y,x) in cdts ] 
print(max(scores))
