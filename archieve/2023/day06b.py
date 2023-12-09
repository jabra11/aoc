import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

times = data[0].split(':')[1]
dis = data[1].split(':')[1]

times = list(filter(lambda x: x != '', times.split(' ')))
times = [''.join(times)]
times = [int(x) for x in times]
dis = list(filter(lambda x: x != '', dis.split(' ')))
dis = [''.join(dis)]
dis = [int(x) for x in dis]

records = list(zip(times,dis))

answ = 1
for time,dis in records:
    ctr = 0
    for hold in range(0,time):
        ndis = (time-hold)*hold
        if ndis>dis:
            ctr+=1
    answ *= ctr

print(answ)
