import sys; datafilepath = sys.argv[1]
lines = open(datafilepath).read().splitlines()

points = {')':3, ']':57, '}':1197, '>':25137}

pairs = {'(':')','<':'>','[':']','{':'}',
         ')':'(','>':'<',']':'[','}':'{'}

ans = 0
for i in lines:
    s = list()
    for j in i:
        if j in ['(','<','[','{']:
            s.append(j)
        else:
            if len(s) == 0:
                continue
            top = s[len(s)-1]
            s.pop()
            
            if j != pairs[top]:
                ans += points[j]
                break
print(ans)
