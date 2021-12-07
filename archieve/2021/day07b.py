pos = [ int(x) for x in open('etc/in').read().split(',') ]

min = min(pos)
max = max(pos)

low = 9999999999999

for i in range(min, max+1):
    s=0
    for j in pos:
        dif = abs(j-i)+1
        s += dif*(dif-1)/2
    if s<low:
        low=s
print(low)
