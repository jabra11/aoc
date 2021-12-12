paths = [ tuple(x.split('-')) for x in open('etc/in').read().splitlines() ]

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

def find_paths(cur_p, end, visited, ctr):
    cur = cur_p[len(cur_p)-1]
    if cur == end:
        all_paths.append(cur_p)
        return
    else:
        for next in (g[cur]):
            ctr2=ctr
            if not (cur,next) in visited:
                visited[(cur,next)] = 0

            if visited[(cur,next)] <= 2:
                tmp = visited.copy()

                if (cur,next) in tmp:
                    tmp[(cur,next)]+=1
                else:
                    tmp[(cur,next)]=1

                if cur.lower() == cur:
                    if (cur,cur) in tmp:
                        tmp[(cur,cur)]+=1
                        ctr2+=1
                        if ctr2 == 2:
                            return
                    else:
                        tmp[(cur,cur)]=1

                    if tmp[(cur,cur)] >= 3:
                        return

                find_paths(cur_p.copy() + [next], end, tmp, ctr2)

s = ['start']
vis = dict()
vis[(None,'start')] = 1

find_paths(s, 'end', vis, 0)

ctr=0
for p in all_paths:
    his = dict()
    if p.count('start') > 1 or p.count('end') > 1:
        continue
    ctr+=1

print(ctr)
