import sys; datafilepath = sys.argv[1]
data = [] 
for i in open(datafilepath).read().splitlines():
    data.append(i)

gamma = ""

for i in range(len(data[0])):
    ctr0=0
    ctr1=0

    for j in range(len(data)):
        if data[j][i] == '0':
            ctr0+=1
        else:
            ctr1+=1

    if ctr0 > ctr1:
        gamma += '0'
    else:
        gamma += '1'

g = int(gamma, 2)
e = g ^ int("1" * len(gamma), 2)

print(g*e)
