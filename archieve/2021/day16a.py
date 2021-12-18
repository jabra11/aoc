data = open('etc/in').read().splitlines()[0]
xmis = ""
for i in data:
    xmis += str(bin(int(i,16)))[2:].zfill(4)

def ceil(n):
    if int(n) == n:
        return n
    return int(n)+1

versions=list()

def parse_next(xmis, start):
    cur = start
    ver = int(xmis[cur:cur+3],2)
    versions.append(ver)
    cur+=3
    tid = int(xmis[cur:cur+3],2)
    cur+=3


    # literal value
    if tid == 4:
        tmp=""
        while xmis[cur] != '0':
            cur+=1
            tmp+=xmis[cur:cur+4]
            cur+=4
        cur+=1
        tmp += xmis[cur:cur+4]
        cur+=3
        return cur+1

    # operator packet
    else:
        tlid = int(xmis[cur])
        cur+=1
        if tlid == 0:
            bitlen = int(xmis[cur:cur+15],2)
            cur+=15
            tmp = cur
            while tmp != cur+bitlen:
                tmp=parse_next(xmis, tmp)
            cur = tmp
        else:
            numpack = int(xmis[cur:cur+11],2)
            cur+=11
            for _ in range(0,numpack):
                cur = parse_next(xmis, cur)

    return cur

parse_next(xmis, 0)
print(sum(versions))
