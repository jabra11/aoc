def main():
    input=open("etc/data.txt").read().splitlines()

    depart = int(input[0])
    buses = []

    for i in input[1].split(','):
        if i != 'x':
            buses.append(int(i))

    best_id = 0
    min = 999999999999999

    for i in buses:
        tmp = 0
        while tmp <= depart: 
            tmp += i

        if tmp - depart < min:
            min = tmp - depart
            best_id = i

    print(best_id)
    print(min)
    

main()
