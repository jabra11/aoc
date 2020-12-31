import math

def main():
    starting_numbers = [1,0,18,10,19,6]
    ctr=1
    
    m = {}

    for i in range(len(starting_numbers)-1):
        m[starting_numbers[i]] = ctr
        ctr+=1

    last = starting_numbers[len(starting_numbers)-1]

    while ctr<=2020:
        print("ctr : {}".format(ctr), end=' ')
        if last in m:
            new_num = ctr - m[last] 
            print("last: {} existed with age {}, overwriting it with age {} \
                and new last is {}-{}={}".format(last,m[last], ctr, ctr,m[last],new_num))
            m[last] = ctr
            last = new_num
        else:
            print("last was {} and is new, thus adding {} at age {}".format(last,last,ctr))
            m[last] = ctr
            last = 0

        ctr+=1

    print(last)



main()
