import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

answ = 0

matches = [0] * 1000
dp = [0] * 1000

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

    dp[cid] += 1
    ctr = 0
    for i in winners:
        if i in actual:
            ctr+=1
    matches[cid] = ctr


for i in range(300):
    for j in range(matches[i]):
        dp[i+j+1] += dp[i]

print(sum(dp))
