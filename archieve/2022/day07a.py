import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().split('$')[1:]
data = [ x.split('\n') for x in data ]

fs = {}
rfs = {}

cdir=('/',0)
fs[cdir] = list()
rfs[cdir] = None

dirs=set()
dirs.add(cdir)

for i in data:
    cmd,out = i[0].lstrip(), i[1:]
    if cmd == 'ls':
        for o in out:
            if len(o) == 0:
                continue
            t,n = o.split(' ')
            if t == 'dir':
                idx=0
                for i in fs.keys():
                    if i[0] == n:
                        idx = max(idx,i[1]+1)
                n = (n,idx)
                fs[n] = list()
                rfs[n] = cdir
                fs[cdir].append(n)
            else:
                fs[cdir].append((t,n))
    else:
        to = cmd.split(' ')[1]
        if to == '..':
            cdir = rfs[cdir]
        else:
            for i in fs[cdir]:
                if i[0] == to:
                    cdir = i


cache={}

def count(head):
    if head in cache:
        return cache[head]
    s=0

    for i in fs[head]:
        n,t = i
        if n.isdigit():
            s+=int(n)
        else:
            tmp=count((n,t))
            cache[(n,t)] = tmp
            s+=tmp

    return s

count(('/',0))

ans=0

for i in cache.keys():
    v = cache[i]
    if v<=100000:
        ans+=v
print(ans)
