def main():
    numbers = open("data.txt").readlines()

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i][:-1])

    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
            for k in range(j, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    print(numbers[i] * numbers[j] * numbers[k])

main()
