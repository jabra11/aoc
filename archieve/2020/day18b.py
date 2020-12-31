def eval(s):
    print("exp: {}".format(s))

    os = []
    ns = []

    i = 0
    while i < len(s):
        num = False
        if s[i] == '+' or s[i] == '*':
            os.append(s[i])
        elif s[i] == '(':
            ctr=1
            j=i+1
            while j < len(s):
                if s[j] == '(':
                    ctr+=1
                elif s[j] == ')':
                    ctr-=1
                    if ctr == 0:
                        ns.append(eval(s[i+1:j]))
                        i=j
                        num = True
                        break
                j+=1
        else:
            j=i
            num = ''
            while j < len(s) and s[j].isdigit():
                num+=s[j]
                j+=1
            i = j-1
            num = int(num)
            ns.append(num)
            num = True

        if num:
            if len(os) > 0:
                lo = os.pop()
                if lo == '+':
                    num = ns.pop()
                    ln = ns.pop()
                    ns.append(num+ln)
                else:
                    os.append(lo)
                    
        i+=1

    ans = 1
    for i in ns:
        ans *= i
    return ans

 
def main():

    ans = 0

    inp = open('etc/data.txt').read().splitlines()
    for i in inp:
        i = i.replace(' ', '')
        res = eval(i)
        ans += res
        print(res)


    print("sum: ", ans)


main()
