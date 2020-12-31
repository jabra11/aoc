def main():
    ratings = []
    for i in open('etc/data.txt').read().splitlines():
        ratings.append(int(i))

    ratings = sorted(ratings)

    ctr1=0
    ctr3=1

    cur = 0

    print(ratings)

    for i in ratings:
        if i - cur >= 1 and i - cur <= 3:
            if i - cur == 1: 
                ctr1+=1
            elif i - cur == 3:
                ctr3+=1
            cur = i


    

    print("ctr1: {}, ctr3: {}".format(ctr1, ctr3))
    print("anw: {}".format(ctr3*ctr1))


    

main()
