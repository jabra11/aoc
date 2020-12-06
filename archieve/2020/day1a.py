def main():
    numbers = open("data.txt").readlines()

    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i][:-1])

    for i in range(0, len(numbers)):
        for j in range(i, len(numbers)):
                if numbers[i] + numbers[j] == 2020:
                    print(numbers[i] * numbers[j])

main()
