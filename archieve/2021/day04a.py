import sys; datafilepath = sys.argv[1]
data = [] 
for i in open(datafilepath).read().splitlines():
    data.append(i)

draws = data[0].split(',')

boards = list()
tmp = list()

for i in range(1,len(data)):
    line = data[i].split('\n\n')
    if line == ['']:
        boards.append(tmp.copy())
        tmp.clear()
    else:
        tmp.append(line)
boards.append(tmp.copy())

for i in range(len(boards)):
    for j in range(len(boards[i])):
        boards[i][j] = boards[i][j][0].split(' ')
        tmp = []
        for k in boards[i][j]:
            if k != '':
                tmp.append((k,False))
        boards[i][j]=tmp.copy()


boards = boards[1:]
winner = list()

cur_draw = 0
while cur_draw < len(draws):
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            for k in range(len(boards[i][j])):
                if boards[i][j][k][0] == draws[cur_draw]:
                    boards[i][j][k] = (draws[cur_draw], True)

    # check rows
    for i in range(len(boards)):
        for j in range(len(boards[i])):
            xctr=0;
            for k in range(len(boards[i][j])):
                if boards[i][j][k][1] == True:
                    xctr += 1
            if xctr==5:
                winner = boards[i]
                break

        for j in range(len(boards[i])):
            yctr=0;
            for k in range(len(boards[i][j])):
                if boards[i][k][j][1] == True:
                    yctr += 1
            if yctr==5:
                winner = boards[i]
                break
    if len(winner) != 0:
        break
    cur_draw += 1

res = 0
for i in winner:
    for j in i:
        if j[1] == False:
            res += int(j[0])
print(res*int(draws[cur_draw]))
