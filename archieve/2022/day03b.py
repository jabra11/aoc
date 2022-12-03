import sys; datafilepath = sys.argv[1]
rs = [list(s) for s in open(datafilepath).read().splitlines()]
rs_c = [ rs[i:i+3] for i in range(0,len(rs),3) ]
rs_s = [ list(set.intersection(set(rss[0]),set(rss[1]), set(rss[2])))[0] for rss in rs_c ]
ans = [list(map(lambda c : ord(c) - ord('A')+27 if ord(c) <= ord('Z') else ord(c) - ord('a')+1, c))[0] for c in rs_s]
print(sum(ans))
