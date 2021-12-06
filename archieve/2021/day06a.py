fishs = [int(x) for x in open('etc/in').read().split(',')]

for i in range(0,80):
    for j in range(len(fishs)):
        if fishs[j] == 0:
            fishs[j] = 6
            fishs.append(8)
        else:
            fishs[j] -= 1

print(len(fishs))
