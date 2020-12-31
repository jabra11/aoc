
def main():
    numbers = open('etc/data.txt').read().splitlines()
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])


    preamble_length = 25
    valid_range = 25


    for i in range(preamble_length, len(numbers)):
        current = numbers[i]
        good = False
        for j in range(i-valid_range, i):
            for k in range(j, i):
                if not numbers[j] == numbers[k]:
                    if numbers[j] + numbers[k] == current:
                        good = True

        if not good:
            print("first invalid num: {}".format(current))



        





main()
