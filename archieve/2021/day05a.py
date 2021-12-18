import sys; datafilepath = sys.argv[1]
data = [] 
for i in open(datafilepath).read().splitlines():
    data.append(i)

lines = [[tuple(map(int,a.split(','))),tuple(map(int,b.split(',')))] 
        for a,b in [line.split(' -> ') for line in data]]

maxy=0
maxx=0
for i in lines:
    for j in i:
        if j[0] > maxx:
            maxx=j[0]
        if j[1] > maxy:
            maxy = j[1]

board = list()
for y in range(maxy+1):
    tmp = [0]*(maxx+1)
    board.append(tmp.copy())

for (s,e) in lines:
    if s[0] == e[0]:
        for j in range(min(s[1],e[1]), max(s[1],e[1])+1):
            board[j][s[0]] += 1
    elif s[1] == e[1]:
        for j in range(min(s[0],e[0]), max(s[0],e[0])+1):
            board[s[1]][j] += 1

ctr=0
for y in board:
    for x in y:
        if x >= 2:
            ctr+=1
print(ctr)
