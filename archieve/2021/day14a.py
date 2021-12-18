import sys; datafilepath = sys.argv[1]
data = [x for x in open(datafilepath).read().splitlines()]

templ = list(data[0])

rules = { x.split(' -> ')[0]: x.split(' -> ')[1] for x in data[2:] }

for i in range(0,10):
    tmp = templ.copy()
    offs = 0
    for i in range(len(templ)-1):
        s = templ[i]+templ[i+1]
        if s in rules:
            tmp.insert(i+1+offs, rules[s])
            offs += 1

    templ = tmp

max = templ.count(max(set(templ), key=templ.count))
min = templ.count(min(set(templ), key=templ.count))
print(max-min)
