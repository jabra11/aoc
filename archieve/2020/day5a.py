def main():
    passes = open('data.txt').readlines()

    for i in range(0, len(passes)):
        passes[i] = passes[i][:-1]

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

        if id > max:
            max = id

    print(max)

main()
