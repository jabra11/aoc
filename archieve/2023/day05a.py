import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().removesuffix('\n')

maps = data.split('\n\n')

maps = [ x.split('\n') for x in maps ]
seeds = maps[0]
maps = [ x[1:] for x in maps[1:] ]
maps = [[y.split(' ') for y in x] for x in maps ]
maps = [[[int(z) for z in y if z != ''] for y in x] for x in maps ]



seeds = seeds[0].split(' ')[1:]
seeds = [ int(x) for x  in seeds ]

def lookup(n, depth):
    if depth == len(maps):
        return n
    for dest,src,le in maps[depth]:
        if n >= src and n <= src+le:
            return lookup(dest+n-src,depth+1)
    return lookup(n, depth+1)


locs = [ lookup(seed,0) for seed in seeds ]
print(min(locs))
