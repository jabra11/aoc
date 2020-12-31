
def main():
    numbers = open('etc/data.txt').read().splitlines()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])


    preamble_length = 25
    valid_range = 25

    invalid = 0

    for i in range(preamble_length, len(numbers)):
        current = numbers[i]
        good = False
        for j in range(i-valid_range, i):
            for k in range(j, i):
                if not numbers[j] == numbers[k]:
                    if numbers[j] + numbers[k] == current:
                        good = True

        if not good:
            invalid = current
            break
    
    s = [1,2,3]

    for i in range(len(numbers)):
        s.append(numbers[i])
        for j in range(i+1, len(numbers)):
            s.append(numbers[j])
            if sum(s) == invalid:
                print(min(s) + max(s))
            elif sum(s) > invalid:
                s = []
                break


main()
