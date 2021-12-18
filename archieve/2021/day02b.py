import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

hor_pos = 0
depth = 0
aim = 0

for m in data:
    if m[0] == 'f':
        hor_pos += int(m[len(m)-1])
        depth += aim *int(m[len(m)-1]) 
    elif m[0] == 'u':
        aim -= int(m[len(m)-1])
    else:
        aim += int(m[len(m)-1])

print(hor_pos*depth)
