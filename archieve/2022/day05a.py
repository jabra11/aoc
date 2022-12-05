import sys, re; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

split = data.index('')
stacks, moves = data[0:split-1], data[split+1:]
stacks = [re.findall(r'\w|\s{4}', i) for i in stacks]
stacks = [ list(reversed(list(map(lambda s: s[i][0], stacks)))) for i in range(len(stacks)+1)]
s = [ list(filter(lambda s: s!= ' ', x)) for x in stacks]

for i in moves:
    n,f,t = list(map(lambda x: int(x), re.findall(r'\d+', i)))
    n,f,t = n,f-1,t-1
    for i in range(n):
        s[t].append(s[f][len(s[f])-1])
        s[f].pop()

for i in s:
    print(i[len(i)-1],end='')
print()
