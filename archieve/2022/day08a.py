import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()
d = data

cnt=0

l=range(len(data))
h=range(len(data[0]))
xm=len(data)
ym=len(data[0])


cdts = [(y,x) for x in l for y in h ]

def good(y,x):
    #r 
    good = True
    for i in range(x+1,xm):
        if d[y][i] >= d[y][x]:
            good=False 
            break
    if good:
        return good
    #l
    good = True
    for i in range(0,x):
        if d[y][i] >= d[y][x]:
            good=False 
            break
    if good:
        return good

    #u
    good = True
    for i in range(y+1,ym):
        if d[i][x] >= d[y][x]:
            good=False 
            break
    if good:
        return good

    #d
    good = True
    for i in range(0,y):
        if d[i][x] >= d[y][x]:
            good=False 
            break
    if good:
        return good

vis = [ 1 for (y,x) in cdts if good(y,x) ] 
print(sum(vis))
