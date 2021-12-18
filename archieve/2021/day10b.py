import sys; datafilepath = sys.argv[1]
lines = open(datafilepath).read().splitlines()

pairs = {'(':')','<':'>','[':']','{':'}',
         ')':'(','>':'<',']':'[','}':'{'}

end_seqs = list()
ans = 0
for i in lines:
    s = list()
    is_valid=True
    for j in i:
        if j in ['(','<','[','{']:
            s.append(j)
        else:
            if len(s) == 0:
                continue
            top = s[len(s)-1]
            s.pop()
            
            if j != pairs[top]:
                is_valid = False
                break
    if is_valid:
        end_seqs.append(s)

points = {')':1, ']':2, '}':3, '>':4}

p = list()
for i in end_seqs:
    if len(i) == 0:
        continue
    anw = 0
    while len(i) > 0:
        top = i[len(i)-1]
        i.pop()
        anw *= 5
        anw += points[pairs[top]]
    p.append(anw)

p = sorted(p)
print(p[int(len(p)/2)])
