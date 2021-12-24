import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()

p1p,p1sc = int(data[0][-1]),0
p2p,p2sc = int(data[1][-1]),0

rolls=0
dicval=1

import numpy as np
from copy import deepcopy

# dp[p1pos][p2pos][p1points][p2points]
dp = np.zeros((11,11,31,31), dtype=int)
dp[p1p][p2p][0][0] = 1

def conti(dp):
    su=0
    for p2pos in dp[1:]:
        for p1points in p2pos[1:]:
            for p2point2 in p1points[0:21]:
                for val in p2point2[0:21]:
                    su += val
    return su != 0

def m10a(n):
    if n == 10:
        return n
    else:
        return n%10

while conti(dp):
    tmp = deepcopy(dp)
    for i in range(1,11):
        for j in range(1,11):
            for k in range(0,21):
                for l in range(0,21):
                    val = tmp[i][j][k][l]
                    if val != 0:
                        for roll1 in range(1,4):
                            for roll2 in range(1,4):
                                for roll3 in range(1,4):
                                    dp[m10a(i+roll1+roll2+roll3)][j][k+m10a(i+roll1+roll2+roll3)][l] += val
                    dp[i][j][k][l] -= val

    tmp = deepcopy(dp)
    for i in range(1,11):
        for j in range(1,11):
            for k in range(0,21):
                for l in range(0,21):
                    val = tmp[i][j][k][l]
                    if val != 0:
                        for roll1 in range(1,4):
                            for roll2 in range(1,4):
                                for roll3 in range(1,4):
                                    dp[i][m10a(j+roll1+roll2+roll3)][k][l+m10a(j+roll1+roll2+roll3)] += val
                    dp[i][j][k][l] -= val

sum = 0
for i in range(1,11):
    for j in range(1,11):
        for k in range(21,31):
            for l in range(0,21):
                sum += dp[i][j][k][l]
print(sum)
