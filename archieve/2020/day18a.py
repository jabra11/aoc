
def evaluate(s):
    su = 0
    last_op = '+'
    i = 0
    while i < len(s):
        if s[i] == '+':
            last_op = '+'
        elif s[i] == '*':
            last_op = '*'
        elif s[i] == ')':
            print("returning on )")
            return su,i

        elif s[i] == '(':
            print("calling on (")
            if last_op == '+':
                new_s, new_i = evaluate(s[i+1:])
                su += new_s 
                i += new_i + 1

            elif last_op == '*':
                new_s, new_i = evaluate(s[i+1:])
                su *= new_s 
                i += new_i + 1
            else:
                print("last op not set!")

        else:
            if last_op == '+':
                su += int(s[i])
            elif last_op == '*':
                su *= int(s[i])
            else:
                print("last op not set (normal)!")


        i+=1

    return su




def main():
    inp = open("etc/data.txt").read().splitlines()

    ans = 0
    for i in inp:
        i = i.replace(' ', '')
        tmp = evaluate(i)
        ans += tmp
        
    print(ans)






main()
