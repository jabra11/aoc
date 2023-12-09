import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

answ = 0

for card in data:
    cid, numbers = card.split(':')
    cid = int(cid[4:])
    winners, actual = numbers.split('|') 
    winners = winners.strip().split(' ')
    winners = [ x for x in winners if x != '' ]
    winners = [int(x) for x in winners]
    actual = actual.strip().split(' ')
    actual = [ x for x in actual if x != '' ]
    actual = [int(x) for x in actual]

    matches = []
    for i in winners:
        if i in actual:
            matches.append(i)

    answ += int(2**(len(matches)-1))

print(answ)
