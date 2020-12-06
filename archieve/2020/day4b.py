def validate(entry, data):
    useful = '' 
    for c in data:
        if c != ' ' and c != '\n':
            useful += c
        else:
            break

    print("entry <{}>, data <{}>".format(entry,useful))
        
    if entry == 'byr':
        year = int(useful)
        valid = (year >= 1920 and year <= 2002)
        if valid:
            print('byr valid')
            return True
        else:
            print('byr invalid')
            return False

    elif entry == 'iyr':
        year = int(useful)
        valid =  (year >= 2010 and year <= 2020)
        if valid:
            print('iyr valid')
            return True
        else:
            print('iyr invalid')
            return False

    elif entry == 'eyr':
        year = int(useful)
        valid =  (year >= 2020 and year <= 2030)

        if valid:
            print('eyr valid')
            return True
        else:
            print('eyr invalid')
            return False

    elif entry == 'ecl':
        c = useful
        valid =  (c == 'amb' or c == 'blu' or c == 'brn'
                or c == 'gry' or c == 'grn' or c == 'hzl'
                or c == 'oth')
        if valid:
            print('ecl valid')
            return True
        else:
            print('ecl invalid')
            return False
    elif entry == 'pid':
        if (len(useful) == 9):
            for i in useful[1:]:
                if not (int(i) >= 0 and int(i) <= 9):
                    return False
            print('pid valid')
            return True
        else:
            print('pid invalid')
            return False

    elif entry == 'hcl':
        valid = True
        if useful[0] == '#':
            for i in useful[1:]:
                count =  ['0', '1','2','3','4','5','6','7','8','9','a'
                        ,'b','c','d','e','f'].count(i)

                print("i = {}, count = {}".format(i,count))
                if count != 1:
                    valid = False
        else:
            valid = False

        if valid:
            print('hcl valid')
            return True
        else:
            print('hcl invalid')
            return False


    elif entry == 'hgt':
        valid = False
        if useful[-2:] == 'cm':
            h = int(useful[:-2])
            if h >= 150 and h <= 193:
                valid = True

        elif useful[-2:] == 'in':
            h = int(useful[:-2])
            if h >= 59 and h <= 76:
                valid = True

        if valid:
            print('hgt valid')
            return True

        else:
            print('hgt invalid')
            return False


def main():
    passports = open("data.txt").readlines()

    # ctr needs 7
    valid = 0
    ctr=0
    for passport in passports:
        if passport == '\n':

            if ctr >= 7:
                valid += 1
                print("valid\n\n")
            else:
                print("invalid\n\n")

            ctr=0

        else:
            for i in range(0, len(passport)):
                if passport[i] == ':': 
                    if not (passport[i-3:i] == 'cid'):
                        if validate(passport[i-3:i], passport[i+1:]):
                            ctr+=1

    print(valid)

main()
