import functools
import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

def symb_val(symb):
    if symb.isdigit():
        return int(symb)
    elif symb == 'T':
        return 10
    elif symb == 'J':
        return 1
    elif symb == 'Q':
        return 12
    elif symb == 'K':
        return 13
    else:
        return 14

def value(hand):
    his = dict()

    val = 0
    for i in hand:
        if i in his:
            his[i] += 1
        else:
            his[i] = 1

    k = list(his.keys())
    if len(k) == 1:
        val = 6#15**11
    elif len(k) == 2 and his[k[0]] in [1,4]:
        val = 5#15**10
    elif len(k) == 2 and his[k[0]] in [2,3]:
        val = 4#15**9
    elif 3 in his.values():
        val = 3#15**8
    elif list(his.values()).count(2) == 2:
        val = 2#15**7
    elif 2 in his.values():
        val = 1#15**6
    return val

orders = []

def compr(a,b):
    if a[3] < b[3]:
        return -1
    elif a[3] > b[3]:
        return 1
    else:
        for i in range(5):
            if symb_val(a[0][i]) < symb_val(b[0][i]):
                return -1
            elif symb_val(a[0][i]) > symb_val(b[0][i]):
                return 1
        

for i,l in enumerate(data):
    hand,bid = l.split(' ')
    bid = int(bid)

    tup = (hand,bid,value(hand),value(hand))
    best = tup[2]

    lst = [hand]
    comb = [hand]

    if hand.count('J') == 5:
        comb = ['AAAAA']
    elif hand.count('J') == 4:
        for i in range(len(hand)):
            if hand[i] != 'J':
                comb = ''.join(5*hand[i])
    else:
        while len(lst) > 0:
            cur = lst[-1]
            lst.pop()
            for i,sym in enumerate(cur):
                if sym == 'J':
                    tmp = list(cur)
                    for j in ['2','3','4','5','6','7','8','9','T','Q','K','A']:
                        tmp[i] = j  
                        tmp2 = ''.join(tmp)
                        if tmp2 not in comb:
                            comb.append(tmp2)
                            lst.append(tmp2)
                        tmp[i] = 'J'
    bst = tup[2]
    bst_card = hand
    for c in comb: 
        nval = value(c)
        if (nval > bst):
            bst = nval
            bst_card = c
    tup = (hand,bid,value(hand),bst)
    orders.append(tup)

orders = sorted(orders, key=functools.cmp_to_key(compr))
answ = 0
for i, trip in enumerate(orders):
    answ += (i+1) * trip[1]
print(answ)
