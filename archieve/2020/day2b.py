def main():
    passwords = open("data.txt").readlines()

    ctr = 0
    for password in passwords: 
        low_set = False
        low = ''

        high = ''
        high_set = False

        char = ''
        pw = ''
        for i in range(0, len(password)-1):
            if not low_set:
                if password[i] != '-':
                    low += password[i]
                else:
                    low_set = True

            elif not high_set:
                if password[i] != ' ':
                    high += password[i]
                else:
                    high_set = True

            else:
                char = password[i]
                pw = password[i+2:]
                break

        print(password)

        high = int(high)
        low = int(low)

        ctr2 = 0
        if pw[high] == char:
            ctr2+=1
        if pw[low] == char:
            ctr2+=1

        if ctr2 == 1:
            ctr+=1

    print(ctr)
main()
