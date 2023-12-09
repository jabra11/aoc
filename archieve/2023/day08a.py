import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

instr = list(data[0])
nodes = data[2:]

mp = dict()

for node in nodes:
    src, dests = node.split(' = ')
    l,r = dests.split(',')
    mp[src] = [l[1:], r[1:-1]]


idx = 0
cur = 'AAA'
while cur != 'ZZZ':
    ins = instr[idx%len(instr)]
    idx += 1
    if ins == 'L':
        cur = mp[cur][0]
    else:
        cur = mp[cur][1]

print(idx)
