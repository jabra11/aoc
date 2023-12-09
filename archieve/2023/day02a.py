import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()


answ = 0

for game in data:
    mp = {'red': 12, 'green':13, 'blue':14}
    gid, cubes = game.split(':')
    gid = int(gid[5:])
    cubes = cubes.split(';')
    cubes = [ x.split(',') for x in cubes ]

    good = True
    for draw in cubes:
        for cube in draw:
            cube = cube.strip()
            num, color = cube.split(' ')
            num = int(num)
            if (mp[color] < num):
                good = False
                break
    if good:
        answ += gid

print(answ)
