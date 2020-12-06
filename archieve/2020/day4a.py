def main():
    passports = open("data.txt").readlines()

    # ctr needs 7
    valid = 0
    ctr=0
    for passport in passports:
        if passport == '\n':
            if ctr >= 7:
                valid += 1
            ctr=0

        else:
            for i in range(0, len(passport)):
                if passport[i] == ':': 
                    if not (passport[i-3:i] == 'cid'):
                        ctr+=1

    print(valid)

main()
