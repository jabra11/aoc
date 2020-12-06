def main():
    passes = open('data.txt').readlines()

    for i in range(0, len(passes)):
        passes[i] = passes[i][:-1]

    seats = []

    max = 0

    for p in passes:
        row = 0
        for i in range(0, 7):
            if p[6-i] == 'B':
                row += (2**i)

        
        column = 0
        for i in range(0,4):
            if p[9-i] == 'R':
                column += (2**i)


        id = row*8 + column
        seats.append(id)

        if id > max:
            max = id


    seats = sorted(seats)
    last = seats[0]

    for i in range(1, len(seats)):
        if seats[i] != last+1:
            print("gap between {} and {}".format(seats[i], last))
            last = seats[i]
        else:
            last = seats[i]
    
main()
