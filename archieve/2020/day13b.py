def is_valid(t, idx, id):
    if (t + idx) % id == 0:
        return True
    else:
        return False


def inverse(a, m):
    a = a % m
    for i in range(1, m):
        if (a*i) % m == 1:
            return i


def main():
    input=open("etc/data.txt").read().splitlines()

    depart = int(input[0])
    buses = []

    for i in input[1].split(','):
        if i != 'x':
            buses.append(int(i))
        else:
            buses.append(-1)

    N = 1
    for i in buses:
        if i != -1:
            N *= i

    # this is not accurate last 1000s ????? wtf

    remainders = []
    for i in range(0, len(buses)):
        if buses[i] != -1:
            remainders.append(buses[i]-i)

    n = []
    for i in range(0, len(buses)):
        if buses[i] != -1:
            n.append(buses[i])

    y = []
    for i in n:
        y.append(N/i)

    z = []
    for i in range(len(y)):
        z.append(inverse(y[i], n[i]))

    sol = 0
    for i in range(len(n)):
        sol += remainders[i] * y[i] * z[i]


    print(sol%N)

    #from sympy.ntheory.modular import crt

    #moduli = []
    #remainders = []
    #for i in range(len(buses)):
    #    if buses[i] != -1:
    #        moduli.append(buses[i])
    #        remainders.append(buses[i]-i) 

    #print(moduli)
    #print(remainders)
    #print(crt(moduli, remainders))
main()
