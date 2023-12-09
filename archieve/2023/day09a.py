import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()


answ = 0

for his in data:
    his = his.split(' ')
    his = [ int(x) for x in his ]
    
    diff = [his]

    idx=0
    while True:
        ndif = []
        for i in range(0, len(diff[idx])-1):
            ndif.append(diff[idx][i+1] - diff[idx][i])
        diff.append(ndif)

        done = True
        for i in ndif:
            if (i != 0):
                done = False
        if done:
            break
        idx+=1

    for i in range(len(diff)-2, -1, -1):
        diff[i].append(diff[i+1][-1]+diff[i][-1])

    answ += diff[0][-1]

print(answ)
