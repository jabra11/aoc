# worst sol ever

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

    wp = {}
    wp['dir1'] = 'E'
    wp['dir2'] = 'N'
    wp['val1'] = 10
    wp['val2'] = 1

    print("wayward: {}{} and {}{}".format(wp['dir1'], 
            wp['val1'],wp['dir2'], wp['val2']))

    print("pos ship {}/{}\n".format(x_pos, y_pos))

    for i in instrucs:
        a,v = parse_instruct(i)

        if (a == 'L' or a == 'R'):
            print("rotating WP {} degs to the {}".format(v, a))
            wp['dir1'] = change_dir(wp['dir1'],a,v)
            wp['dir2'] = change_dir(wp['dir2'],a,v)

        elif a == 'F':
            for i in range(v):
                if wp['dir1'] == 'E':
                    if wp['dir2'] == 'N':
                        x_pos += wp['val1']
                        y_pos += wp['val2']
                    else:
                        x_pos += wp['val1']
                        y_pos -= wp['val2']
                elif wp['dir1'] == 'S':
                    if wp['dir2'] == 'E':
                        y_pos -= wp['val1']
                        x_pos += wp['val2']
                    else:
                        y_pos -= wp['val1']
                        x_pos -= wp['val2']
                elif wp['dir1'] == 'W':
                    if wp['dir2'] == 'S':
                        x_pos -= wp['val1']
                        y_pos -= wp['val2']
                    else:
                        x_pos -= wp['val1']
                        y_pos += wp['val2']
                elif wp['dir1'] == 'N':
                    if wp['dir2'] == 'W':
                        y_pos += wp['val1']
                        x_pos -= wp['val2']
                    else:
                        y_pos += wp['val1']
                        x_pos += wp['val2']
                else:
                    print('lulw')
                    return  0
        else:
            if a == 'N':
                if wp['dir1'] == 'N':
                    wp['val1'] += v
                elif wp['dir1'] == 'S':
                    wp['val1'] -= v
                elif wp['dir2'] == 'N':
                    wp['val2'] += v
                elif wp['dir2'] == 'S':
                    wp['val2'] -= v
            elif a == 'S':
                if wp['dir1'] == 'N':
                    wp['val1'] -= v
                elif wp['dir1'] == 'S':
                    wp['val1'] += v
                elif wp['dir2'] == 'N':
                    wp['val2'] -= v
                elif wp['dir2'] == 'S':
                    wp['val2'] += v

            elif a == 'W':
                if wp['dir1'] == 'W':
                    wp['val1'] += v
                elif wp['dir1'] == 'E':
                    wp['val1'] -= v
                elif wp['dir2'] == 'W':
                    wp['val2'] += v
                elif wp['dir2'] == 'E':
                    wp['val2'] -= v

            elif a == 'E':
                if wp['dir1'] == 'E':
                    wp['val1'] += v
                elif wp['dir1'] == 'W':
                    wp['val1'] -= v
                elif wp['dir2'] == 'E':
                    wp['val2'] += v
                elif wp['dir2'] == 'W':
                    wp['val2'] -= v

            if wp['val1'] < 0:
                wp['dir1'] = change_dir(wp['dir1'], 'R', 180)
                wp['val1'] *= -1

            if wp['val2'] < 0:
                wp['dir2'] = change_dir(wp['dir2'], 'R', 180)
                wp['val2'] *= -1

        print("wayward: {}{} and {}{}".format(wp['dir1'], 
                wp['val1'],wp['dir2'], wp['val2']))

        print("pos ship {}/{}\n".format(x_pos, y_pos))

    print("x:{}, y:{}".format(x_pos, y_pos))
    print("manhatten pos: {}".format(abs(x_pos)+ abs(y_pos)))

main()
