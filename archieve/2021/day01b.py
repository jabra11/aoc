data = [] 
for i in open('etc/in').read().splitlines():
    data.append(int(i))

ctr=0

last = data[0]+data[1]+data[2]
for i in range(3,len(data)):
    cur = data[i]+data[i-1]+data[i-2]
    if cur > last:
        ctr+=1
    last = cur

print(ctr)
