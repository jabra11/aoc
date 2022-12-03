import sys; datafilepath = sys.argv[1]
pts = { 'X': { 'A': 3, 'B': 0, 'C': 6, }, 'Y': { 'A': 6, 'B': 3, 'C': 0, }, 'Z': { 'A': 0, 'B': 6, 'C': 3 } }
m = {'X': 1, 'Y': 2, 'Z':3}
print(sum([pts[b][a] + m[b] for a,b in [x.split(' ') for x in open(datafilepath).read().splitlines()]]))
