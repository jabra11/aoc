pos = [ int(x) for x in open('etc/in').read().split(',') ]

avg = sum(pos)/len(pos)

# should ideally check floor(mean)-1 and floor(mean)+1
s_low=0
s_high=0

for i in pos:
    dif = abs(int(avg)-i)
    s_low += dif*(dif+1)/2

for i in pos:
    dif = abs(int(avg+1)-i)
    s_high += dif*(dif+1)/2
    
print(int(min(s_low, s_high)))
