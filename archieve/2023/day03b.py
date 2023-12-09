import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()


for i in range(0,len(data)):
    data[i] = '.' + data[i] + '.'

s = ''
for i in range(0,len(data[0])):
    s+='.'
data = [s] + data + [s]

isSymbol = lambda x : x == '*'
mp = dict()
answ = 0
for y in range(1,len(data)-1):
    good = False
    cur_dig = ''
    start_pos = (0,0)
    ankers = []
    for x in range(1,len(data[y])-1):
        if (data[y][x].isdigit() and 
            (isSymbol(data[y][x-1]) or isSymbol(data[y][x+1]) or 
             isSymbol(data[y+1][x-1]) or isSymbol(data[y+1][x]) or 
             isSymbol(data[y+1][x+1]) or isSymbol(data[y-1][x-1]) or 
             isSymbol(data[y-1][x]) or isSymbol(data[y-1][x+1]))):
            for k in [-1,0,1]:
                for j in [-1,0,1]:
                    if data[y+k][x+j] == '*':
                        ankers.append((y+k,x+j))
            start_pos = (y,x)
            good = True
        if (data[y][x].isdigit()):
            cur_dig += data[y][x]
        else:
            if good:
                good = False
                if not cur_dig == '':
                    cur_dig = int(cur_dig)
                    for p in ankers:
                        if p in mp:
                            mp[p].add((cur_dig, start_pos))
                        else:
                            mp[p] = set([(cur_dig, start_pos)])
                    cur_dig = ''
                    start_pos = (0,0)
                    ankers=[]
            else:
                cur_dig = ''
                good = False
                start_pos = (0,0)
                ankers=[]

    if cur_dig != '' and good:
        cur_dig = int(cur_dig)
        for p in ankers:
            if p in mp:
                mp[p].add((cur_dig,start_pos))
            else:
                mp[p] = set([(cur_dig, start_pos)])

answ = 0
for gear in mp.keys():
    vals = list(mp[gear])
    if len(vals) != 2:
        continue
    answ += vals[0][0] * vals[1][0]
print(answ)
