def parse_instruct(instruct):
    return instruct[0], int(instruct[1:])

def change_dir(cur, action, val):
    count = val / 90

    for i in range(int(count)):
        if action == 'R':
            if cur == 'N': cur = 'E'
            elif cur == 'E': cur = 'S'
            elif cur == 'S': cur = 'W'
            elif cur == 'W': cur = 'N'
        elif action == 'L':
            if cur == 'N': cur = 'W'
            elif cur == 'W': cur = 'S'
            elif cur == 'S': cur = 'E'
            elif cur == 'E': cur = 'N'

    return cur
            


def main():
    instrucs = open('etc/data.txt').read().splitlines()

    x_pos = 0
    y_pos = 0

    d = 'E'
    for i in instrucs:
        a,v = parse_instruct(i)

        if (a == 'L' or a == 'R'):
            d = change_dir(d, a, v)
        else:
            if a == 'F':
                if d == 'E':
                    x_pos += v
                elif d == 'W':
                    x_pos -= v
                elif d == 'N':
                    y_pos += v
                elif d == 'S':
                    y_pos -= v
            elif a == 'N': y_pos += v
            elif a == 'S': y_pos -= v
            elif a == 'E': x_pos += v
            elif a == 'W': x_pos -= v


    print("x:{}, y:{}".format(x_pos, y_pos))
    print("manhatten pos: {}".format(abs(x_pos)+ abs(y_pos)))


main()
