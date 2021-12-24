import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

p1pos,p1score = int(data[0][-1]),0
p2pos,p2score = int(data[1][-1]),0

rolls=0
dicval=1

while True:

    tmp = 0
    for i in range(3):
        tmp += dicval
        dicval+=1
        rolls+=1
    p1pos = (p1pos + tmp) % 10
    p1score += p1pos

    if p1score >= 1000:
        break

    tmp = 0
    for i in range(3):
        tmp += dicval
        dicval+=1
        rolls+=1
    p2pos = (p2pos + tmp) % 10
    p2score += p2pos

    if p2score >= 1000:
        break

print(rolls*min(p1score,p2score))
