import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()


for i in range(0,len(data)):
    data[i] = '.' + data[i] + '.'

s = ''
for i in range(0,len(data[0])):
    s+='.'
data = [s] + data + [s]

isSymbol = lambda x : not (x.isdigit() or x == '.')

answ = 0
for y in range(1,len(data)-1):
    good = False
    cur_dig = ''
    for x in range(1,len(data[y])-1):
        if (data[y][x].isdigit() and 
            (isSymbol(data[y][x-1]) or isSymbol(data[y][x+1]) or 
             isSymbol(data[y+1][x-1]) or isSymbol(data[y+1][x]) or 
             isSymbol(data[y+1][x+1]) or isSymbol(data[y-1][x-1]) or 
             isSymbol(data[y-1][x]) or isSymbol(data[y-1][x+1]))):
            good = True
        if (data[y][x].isdigit()):
            cur_dig += data[y][x]
        else:
            if good:
                good = False
                if not cur_dig == '':
                    answ += int(cur_dig)
                    cur_dig = ''
            else:
                cur_dig = ''
                good = False

    if cur_dig != '' and good:
        answ += int(cur_dig)

    
print(answ)
