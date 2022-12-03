import sys; datafilepath = sys.argv[1]
rs = open(datafilepath).read().splitlines()
rs_c = [ (r[:len(r)//2], r[len(r)//2:]) for r in [ list(s) for s in rs] ]
rs_s = [ list(set.intersection(set(a),set(b)))[0] for (a,b) in rs_c ]
ans = [list(map(lambda c : ord(c) - ord('A')+27 if ord(c) <= ord('Z') else ord(c) - ord('a')+1, c))[0] for c in rs_s]
print(sum(ans))
