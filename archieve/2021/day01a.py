import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

ctr=0

for i in range(1, len(data)):
    if int(data[i]) > int(data[i-1]): 
        ctr+=1
print(ctr)
