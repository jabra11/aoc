import sys; datafilepath = sys.argv[1]
nums = open(datafilepath).read().splitlines()

def add_nums(lhs,rhs):
    return '[{},{}]'.format(lhs,rhs)

def ceil(n):
    if int(n) == n:
        return int(n)
    return int(n)+1

def explode(num, l, r):
    (lhs,rhs) = num[l+1:r].split(',')
    lhs = int(lhs); rhs = int(rhs)
    leftoffs=0
    sl=l-1
    while sl >= 0:
        if num[sl] not in [']','[',',']:
            j = sl-1
            while j >= 0 and num[j] not in [']','[',',']:
                j-=1
            leftnum = int(num[j+1:sl+1])
            num = num[0:j+1] + str(lhs+leftnum) + num[sl+1:]

            leftoffs = len(str(lhs+leftnum)) - len(str(leftnum))
            break
        sl-=1

    sr=r+leftoffs+1
    while sr < len(num):
        if num[sr] not in [']','[',',']:
            j = sr+1
            while j < len(num) and num[j] not in [']','[',',']:
                j+=1
            rightnum = int(num[sr:j])

            num = num[0:sr] + str(rhs+rightnum) + num[j:]

            break
        sr+=1
    num = num[0:l+leftoffs] + '0' + num[r+leftoffs+1:]
    return num

def reduce_num(n):
    nums_to_split = list()
    while True:
        i=0
        s = list()
        nums_to_split = list()
        exploded = False
        while i < len(n):
            if n[i] == '[':
                s.append(i)
            elif n[i] == ']':
                if len(s) > 4:
                    lpos = s[len(s)-1]
                    s.pop()
                    #print('exploding')
                    n = explode(n, lpos, i)
                    #print(n)
                    exploded = True
                    break
                s.pop()
            elif n[i] == ',':
                i+=1
                continue
            else:
                j=i+1
                while n[j] not in ['[',']',',']:
                    j+=1
                num = int(n[i:j])
                if num >= 10:
                    nums_to_split.append((num,i,j-1))
                i=j-1
            i+=1

        if not exploded:
            if len(nums_to_split) == 0:
                return n
            offset=0
            for (num,l,r) in nums_to_split[0:1]:
                sub = "[{},{}]".format(num//2, ceil(num/2))
                n = n[0:l+offset] + sub + n[r+1+offset:]
                offset += len(sub) - len(str(num))

def evalu(n):
    lhs=''
    rhs=''
    ctr=0
    for i in range(len(n)):
        if n[i] == '[':
            ctr+=1
        elif n[i] == ']':
            ctr-=1
        elif n[i] == ',':
            if ctr == 1:
                lhs = n[1:i]
                rhs = n[i+1:-1]
    
    if '[' not in lhs:
        if '[' not in rhs:
            return 3*int(lhs) + 2*int(rhs)
        else:
            return 3*int(lhs) + 2*evalu(rhs)
    if '[' not in rhs:
        if '[' not in lhs:
            return 3*int(lhs) + 2*int(rhs)
        else:
            return 3*evalu(lhs) + 2*int(rhs)
    
    return 3*evalu(lhs) + 2*evalu(rhs)


ans = 0
for i in range(len(nums)):
    for j in range(len(nums)):
        if i == j:
            continue
        ans = max(ans, evalu(reduce_num(add_nums(nums[i],nums[j]))))
print(ans)
