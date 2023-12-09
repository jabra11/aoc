import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

def symb_val(symb):
    if symb.isdigit():
        return int(symb)
    if symb == 'T':
        return 10
    if symb == 'J':
        return 11
    if symb == 'Q':
        return 12
    if symb == 'K':
        return 13
    if symb == 'A':
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

    # five of a kind
    if len(k) == 1:
        val = 15**11

    # four of a kind
    elif len(k) == 2 and his[k[0]] in [1,4]:
        val = 15**10

    # full house
    elif len(k) == 2 and his[k[0]] in [2,3]:
        val = 15**9

    # three of a kind
    elif 3 in his.values():
        val = 15**8

    # two pairs
    elif list(his.values()).count(2) == 2:
        val = 15**7

    # 1 pair
    elif 2 in his.values():
        val = 15**6

    for i,card in enumerate(hand):
        val += symb_val(card) * 15**(5-i)
    return val

orders = []

for l in data:
    hand,bid = l.split(' ')
    bid = int(bid)
    orders.append((hand,bid,value(hand)))

orders = sorted(orders, key=lambda trp: trp[2])

answ = 0
for i, trip in enumerate(orders):
    answ += (i+1) * trip[1]

print(answ)
