import sys; datafilepath = sys.argv[1]
paths = [ tuple(x.split('-')) for x in open(datafilepath).read().splitlines() ]

g = dict()

for (a,b) in paths:
    if not a in g:
        g[a] = list()
        g[a].append(b)
    else:
        g[a].append(b)
    if not b in g:
        g[b] = list()
        g[b].append(a)
    else:
        g[b].append(a)

all_paths = []

def find_paths(cur_p, end, visited):
    cur = cur_p[len(cur_p)-1]
    if cur == end:
        all_paths.append(cur_p)
        return
    else:
        for next in (g[cur]):
            if not (cur,next) in visited:
                if cur.lower() == cur:
                    if (cur,cur) in visited:
                        return
                tmp = visited.copy()
                tmp.add((cur,next))
                tmp.add((cur,cur))
                find_paths(cur_p.copy() + [next], end, tmp)

s = ['start']
vis = set()
vis.add((None,'start'))

find_paths(s, 'end', vis)

print(len(all_paths))
