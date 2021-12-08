data = [ x.split('|') for x in open('etc/in').read().splitlines() ]

data2=list()
for i in data:
    data2.append((i[0][:-1].split(' '), i[1][1:].split(' ')))
data=data2

ctr1=0
ctr4=0
ctr7=0
ctr8=0

for i in data:
    for j in i[1]:
        if len(j) == 2:
            ctr1+=1
        elif len(j) == 4:
            ctr4+=1
        elif len(j) == 3:
            ctr7+=1
        elif len(j) == 7:
            ctr8+=1

print(sum([ctr1,ctr4,ctr7,ctr8]))
