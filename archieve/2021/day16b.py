data = open('etc/in').read().splitlines()[0]
xmis = ""
for i in data:
    xmis += str(bin(int(i,16)))[2:].zfill(4)

def ceil(n):
    if int(n) == n:
        return n
    return int(n)+1

global_ctr=0
g = dict()

def parse_next(xmis, start, parent):
    cur = start
    ver = int(xmis[cur:cur+3],2)
    cur+=3
    tid = int(xmis[cur:cur+3],2)
    cur+=3

    global global_ctr
    global_ctr+=1
    if tid == 4:
        tmp=""
        while xmis[cur] != '0':
            cur+=1
            tmp+=xmis[cur:cur+4]
            cur+=4
        cur+=1
        tmp += xmis[cur:cur+4]
        cur+=3
        g[parent].append((global_ctr,tid,int(tmp,2)))

        return cur+1

    else:
        tlid = int(xmis[cur])
        cur+=1
        id=global_ctr
        if tlid == 0:
            bitlen = int(xmis[cur:cur+15],2)
            cur+=15
            tmp = cur
            ctr=0
            g[(id,tid,-1)] = list()
            while tmp != cur+bitlen:
                tmp = parse_next(xmis, tmp,(id,tid,-1))
                ctr+=1
            g[parent].append((id,tid,-1))
            cur = tmp
        else:
            numpack = int(xmis[cur:cur+11],2)
            cur+=11
            g[(id,tid,-1)] = list()
            for _ in range(0,numpack):
                cur = parse_next(xmis, cur,(id,tid,-1))
            g[parent].append((id,tid,-1))

    return cur

g['start'] = list()
parse_next(xmis, 0, 'start')

def evalu(start):
    cur = (ctr,id,val) = start
    
    if (id == 4):
        return val

    if id == 0:
        sum = 0    
        for i in g[cur]:
            sum += evalu(i)
        return sum
    elif id == 1:
        prod = 1
        for i in g[cur]:
            prod *= evalu(i)
        return prod
    elif id == 2:
        l = list()
        for i in g[cur]:
            l.append(evalu(i))
        return min(l)
    elif id == 3:
        l = list()
        for i in g[cur]:
            l.append(evalu(i))
        return max(l)
    elif id == 5:
        first = evalu(g[cur][0])
        second = evalu(g[cur][1])
        if first > second:
            return 1
        else:
            return 0
    elif id == 6:
        first = evalu(g[cur][0])
        second = evalu(g[cur][1])
        if first < second:
            return 1
        else:
            return 0
    elif id == 7:
        first = evalu(g[cur][0])
        second = evalu(g[cur][1])
        if first == second:
            return 1
        else:
            return 0



s = g['start']
print(evalu(s[0]))
