import sys; datafilepath = sys.argv[1]
data = list(open(datafilepath).read().splitlines()[0])

s = [ (set(data[i:i+4]), i+4) for i in range(len(data)-1) ]
s = [ n for (s,n) in s if len(s) == 4 ]
print(s[0])
