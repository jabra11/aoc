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

    for i in inp:
        i = i.split(',')
        
        for j in i:
            good = False
            j = int(j)
            print("testing {}".format(j))
            for low, high in rules:
                if j >= low and j <= high:
                    good = True 
                    break
                    
            if good == False:
                print("{} is invalid".format(j))
                ctr+=j


    print(ctr)
    
        





main()
