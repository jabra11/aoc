data = [x for x in open('etc/in').read().splitlines()]
rules = { x.split(' -> ')[0]: x.split(' -> ')[1] for x in data[2:] }
pm = dict()
for i in range(len(data[0])-1):
    pm[data[0][i]+data[0][i+1]] = 1

for i in range(0,40):
    tmp = pm.copy()
    for k in pm.keys():
        if pm[k] == 0:
            continue
        if k in rules:
            tmp[k] -= pm[k]
            if k[0] + rules[k] in tmp:
                tmp[k[0]+rules[k]] += pm[k]
            else:
                tmp[k[0]+rules[k]] = pm[k]

            if rules[k]+k[1] in tmp:
                tmp[rules[k]+k[1]] += pm[k]
            else:
                tmp[rules[k]+k[1]] = pm[k]
    pm = tmp

his = dict()
for i in pm.keys():
    for j in i:
        his[j] = 0

for i in pm.keys():
    for j in i:
        his[j] += pm[i]

his[data[0][0]] += 1
his[data[0][len(data[0])-1]] += 1

ctr=0
for k in his.keys():
    his[k] = int(his[k]/2)
    ctr+=his[k]

print(int(max(his.values()) - min(his.values())))
