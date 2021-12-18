import sys; datafilepath = sys.argv[1]
fishs = [int(x) for x in open(datafilepath).read().split(',')]

for i in range(0,4):
    for j in range(len(fishs)):
        if fishs[j] == 0:
            fishs[j] = 6
            fishs.append(8)
        else:
            fishs[j] -= 1

zdict = dict()
for i in range(9):
    zdict[i]=0
m = zdict.copy()

for i in fishs:
    if i in m:
        m[i] += 1

for i in range(0,36):
    mtmp = zdict.copy()

    for i in m.keys():
        if i > 6:
            m[i%7] += m[i]
            m[i] = 0
        else:
            mtmp[i+2] += m[i]

    for i in mtmp.keys():
        m[i] += mtmp[i]

print(sum(m.values()))
