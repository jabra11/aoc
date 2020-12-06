def main():
    answers = open("data.txt").readlines()

    for i in range(0, len(answers)):
        if answers[i] != '\n':
            answers[i] = answers[i][:-1]


    ctr = 0
    sett = []
    for i in answers:
        if i == '\n':
            sett = []
            continue

        for j in i:
            if not (j in sett):
                sett.append(j)
                ctr+=1


    print(ctr)


main()
