import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

instr = list(data[0])
nodes = data[2:]

mp = dict()

for node in nodes:
    src, dests = node.split(' = ')
    l,r = dests.split(',')
    mp[src] = [l[1:], r[1:-1]]


cur = []
for i in mp.keys():
    if i[-1] == 'A':
        cur.append(i)

idices = []
for starti in cur:
    idx=0
    st = starti
    while st[-1] != 'Z':
        ins = instr[idx%len(instr)]
        idx += 1
        if ins == 'L':
            st = mp[st][0]
        else:
            st = mp[st][1]
    idices.append(idx)


import math
answ = 1
for i in idices:
    answ = math.lcm(answ,i)
print(answ)
