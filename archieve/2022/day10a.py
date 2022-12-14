import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

xreg = 1
cycle = 0

answ=0

for i in data:
    match i.split(' '): 
        case a,b:
            for _ in range(2):
                cycle+=1
                if cycle == 20 or (cycle-20) % 40 == 0:
                    answ += cycle * xreg
            xreg += int(b)
        case a:
            cycle+=1
            if cycle == 20 or (cycle-20) % 40 == 0:
                answ += cycle * xreg

print(answ)
