import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

val = [1,2,3,4,5,6,7,8,9]
key = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
mp = dict(zip(key,val))
replace = lambda w : [ w :=  w.replace(k,k+str(mp[k])+k) for k in mp.keys() ]
data = [ replace(d)[-1] for d in data ]
data = [ ''.join(filter(str.isdigit,x)) for x in data ]
data = [ int(x[0])*10 + int(x[len(x)-1]) for x in data ]
print(sum(data))
