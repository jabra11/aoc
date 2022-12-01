import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read()

print(max([sum(z) for z in [list(map(lambda x : int(x) if x != '' else 0, set(x.split('\n')))) for x in data.split('\n\n')]]))
