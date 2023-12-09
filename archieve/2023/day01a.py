import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

data = [ ''.join(filter(str.isdigit,x)) for x in data ]
data = [ int(x[0])*10 + int(x[len(x)-1]) for x in data ]
print(sum(data))
