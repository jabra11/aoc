import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

ap = [list(map(lambda y : int(y), y.split('-'))) for x in data for y in x.split(',')] 
ap = [ ap[i:i+2] for i in range(0,len(ap),2) ]
ap = [ a<=c<=d<=b or c<=a<=b<=d for ((a,b),(c,d)) in ap]
print(sum(ap))
