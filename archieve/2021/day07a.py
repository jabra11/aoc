import sys; datafilepath = sys.argv[1]
pos = [ int(x) for x in open(datafilepath).read().split(',') ]

min = min(pos)
max = max(pos)

low = 9999999999999

for i in range(min, max+1):
    s=0
    for j in pos:
        s += abs(j-i)
    if s<low:
        low=s
print(low)
