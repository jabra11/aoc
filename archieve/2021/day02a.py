data = open("etc/in").read().splitlines()

hor_pos = 0
depth = 0

for m in data:
    if m[0] == 'f':
        hor_pos += int(m[len(m)-1])
    elif m[0] == 'u':
        depth -= int(m[len(m)-1])
    else:
        depth += int(m[len(m)-1])

print(hor_pos*depth)
