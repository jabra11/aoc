data = [] 
for i in open('etc/in').read().splitlines():
    data.append(i)

gamma = ""

last = data.copy()
for i in range(len(last[0])):
    tmp = []
    ctr0=0
    ctr1=0

    for j in range(len(last)):
        if last[j][i] == '0':
            ctr0+=1
        else:
            ctr1+=1

    if ctr0 > ctr1:
        for j in range(len(last)):
            if last[j][i] == '0':
                tmp.append(last[j])
    else:
        for j in range(len(last)):
            if last[j][i] == '1':
                tmp.append(last[j])

    if len(tmp) == 1:
        oxy = tmp[0]
        break
    else:
        last = tmp.copy()

last = data.copy()
for i in range(len(last[0])):
    tmp = []
    ctr0=0
    ctr1=0

    for j in range(len(last)):
        if last[j][i] == '0':
            ctr0+=1
        else:
            ctr1+=1

    if ctr0 > ctr1:
        for j in range(len(last)):
            if last[j][i] == '1':
                tmp.append(last[j])
    else:
        for j in range(len(last)):
            if last[j][i] == '0':
                tmp.append(last[j])

    if len(tmp) == 1:
        co2 = tmp[0]
        break
    else:
        last = tmp.copy()

print(int(co2, 2) * int(oxy, 2))
