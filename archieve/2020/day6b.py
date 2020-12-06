def main():
    answers = open("data.txt").readlines()

    for i in range(0, len(answers)):
        if answers[i] != '\n':
            answers[i] = answers[i][:-1]


    ctr = 0
    vec = []
    
    member_ctr=0

    for i in answers:
        if i == '\n':
            for j in vec:
                if vec.count(j) == member_ctr:
                    ctr+= 1 / member_ctr

            member_ctr = 0
            vec = []
            continue

        for j in i:
            vec.append(j)

        member_ctr +=1

    print(ctr)

main()
