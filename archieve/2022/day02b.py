import sys; datafilepath = sys.argv[1]
pts = { 'X': { 'A': 'Z', 'B': 'X', 'C': 'Y', }, 'Y': { 'A': 'X', 'B': 'Y', 'C': 'Z', }, 'Z': { 'A': 'Y', 'B': 'Z', 'C': 'X' } }
m = {'X': 0, 'Y': 3, 'Z':6}
mm = {'X': 1, 'Y': 2, 'Z':3}
print(sum([ m[b] + mm[pts[b][a]] for a,b in [ x.split(' ') for x in open(datafilepath).read().splitlines()]]))
