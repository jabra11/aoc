data = [ x.split('|') for x in open('etc/in').read().splitlines() ]

data2=list()
for i in data:
    data2.append((i[0][:-1].split(' '), i[1][1:].split(' ')))
data=data2

#    0:      1:      2:      3:      4:
#   aaaa    ....    aaaa    aaaa    ....
#  b    c  .    c  .    c  .    c  b    c
#  b    c  .    c  .    c  .    c  b    c
#   ....    ....    dddd    dddd    dddd
#  e    f  .    f  e    .  .    f  .    f
#  e    f  .    f  e    .  .    f  .    f
#   gggg    ....    gggg    gggg    ....
#  
#    5:      6:      7:      8:      9:
#   aaaa    aaaa    aaaa    aaaa    aaaa
#  b    .  b    .  .    c  b    c  b    c
#  b    .  b    .  .    c  b    c  b    c
#   dddd    dddd    ....    dddd    dddd
#  .    f  e    f  .    f  e    f  .    f
#  .    f  e    f  .    f  e    f  .    f
#   gggg    gggg    ....    gggg    gggg

# 1:2 
# 7:3 
# 4:4
#
# 2:5, 3:5, 5:5
# 0:6, 6:6, 9:6
#
# 8:7 

answer=0
for i in data:
    nums = dict()
    map = dict()

    wir = i[0]
    out = i[1]

    for i in ['a','b','c','d','e','f','g']:
        map[i] = set()

    for i in range(0,10):
        map[i] = set()

    # get 1,7,4,8
    for i in wir:
        l = len(i)

        if len(i) == 2:
            nums[1] = set(i)
        if len(i) == 3:
            nums[7] = set(i)
        if len(i) == 4:
            nums[4] = set(i)
        if len(i) == 7:
            nums[8] = set(i)
    
    map['a'] = nums[7]-nums[1]
    map['c'] = nums[1]
    map['f'] = nums[1]

    map['b'] = nums[4]-nums[1]
    map['d'] = nums[4]-nums[1]

    # get 2,5,6
    posis = []
    for i in wir:
        ctr=0
        for j in map['c']:
            if j in i:
                ctr+=1
        if ctr == 1:
            posis.append(i)

    for i in posis:
        if len(i) == 6:
            nums[6] = set(i)

    for i in posis:
        if len(nums[6] - set(i)) == 1:
            nums[5] = set(i)
        elif len(nums[6] - set(i)) == 2:
            nums[2] = set(i)

    map['e'] = nums[6]-nums[5]-nums[1]
    nums[9] = nums[8] - map['e']

    # we have 1,2,4,5,6,7,8,9
    # we need 0,3

    map['b'] = (nums[8]-nums[2])-nums[1]
    map['d'] = map['d'] - map['b']
    nums[0] = nums[8] - map['d']
        
    # need 3
    nums[3] = (nums[8] - map['b']) - map['e']
     
    res = ""
    for n in out:
        found = 0
        for j in range(0,10):
            if set(n) == set(nums[j]):
                found=1
                res += str(j)
        if found==0:
            print(n)

    answer += int(res)

print(answer)
