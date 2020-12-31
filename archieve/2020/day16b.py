import math

def main():
    inp = open("etc/data2.txt").read().splitlines()

    rules = []
    for i in inp:
        
        first_num=0
        second_num=0
        third_num=0
        forth_num=0

        j = 0
        while j < len(i):
            if i[j] == ':':
                j+=1
                break
            j+=1

        k = j
        while k < len(i):
            if i[k] == '-':
                break
            k+=1
        first_num = int(i[j:k])

        k+=1
        j=k
        while k < len(i):
            if i[k] == ' ':
                break
            k+=1
        second_num = int(i[j:k])

        k+=4
        j=k
        while k < len(i):
            if i[k] == '-':
                break
            k+=1
        third_num = int(i[j:k])

        k+=1
        j=k
        while k < len(i):
            if i[k] == ' ':
                break
            k+=1
        forth_num = int(i[j:k])

        rules.append((first_num, second_num))
        rules.append((third_num, forth_num))

    inp = open("etc/data.txt").read().splitlines()
    
    ctr=0

    valid_tickets = []

    for i in inp:
        i = i.split(',')
        all_good = True 
        for j in i:
            good = False
            j = int(j)
            print("testing {}".format(j))
            for low, high in rules:
                if j >= low and j <= high:
                    good = True 
                    break
                    
            if good == False:
                all_good = False
                print("{} is invalid".format(j))
                ctr+=j
        
        if all_good:
            valid_tickets.append(i)
        else:
            print("bad")

    
    my_ticket = '79,193,53,97,137,179,131,73,191,139,197,181,67,\
    71,211,199,167,61,59,127'.split(',')

    valid_tickets.append(my_ticket)

    for i in range(len(my_ticket)):
        my_ticket[i] = int(my_ticket[i])

    for i in valid_tickets:
        for j in range(len(i)):
            i[j] = int(i[j])

    m = {}

    for i in range(0, len(rules),2):
        m[int(i/2+1)] = []

        low1,high1 = rules[i]
        low2,high2 = rules[i+1]

        field = 0
        while field < 20:
            all_good= True
            for j in valid_tickets:
                val = j[field]
                if not ((val >= low1 and val <= high1) or (val >= low2 and val <= high2)):
                    all_good = False
                    print("field {} can't belong to rule {}".format(field, int(i/2+1)))
                    break
                 
            if (all_good):
                print("field {} can belong to rule {}".format(field, int(i/2+1)))
                m[int(i/2+1)].append(field)
                
            field+=1

    for i in m:
        print("valid fields for {}: {}".format(i, m[i]))

    print("starting ordering")

    ordered = False
    while (not ordered):
        ordered = True
        for i in m:
            if len(m[i]) == 1:
                for j in m:
                    if j != i:
                        if m[j].count(m[i][0]) > 0:
                            m[j].remove(m[i][0])
        
        for i in m:
            print("valid fields for {}: {}".format(i, m[i]))

        for i in m:
            good = True
            if len(m[i]) != 1:
                good = False

            if not good:
                ordered = False


    ans = 1
    for i in range(1,7):
        ans *= my_ticket[m[i][0]]

    print(ans)

    




main()
