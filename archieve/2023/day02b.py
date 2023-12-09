import sys; datafilepath = sys.argv[1]
data = open(datafilepath).read().splitlines()


answ = 0

for game in data:
    mp = {'red': 0, 'green':0, 'blue':0}
    gid, cubes = game.split(':')
    gid = int(gid[5:])
    cubes = cubes.split(';')
    cubes = [ x.split(',') for x in cubes ]

    for draw in cubes:
        for cube in draw:
            cube = cube.strip()
            num, color = cube.split(' ')
            num = int(num)
            mp[color] = max(mp[color], num)

    pro = 1
    for v in mp.values():
        pro *= v

    answ += pro

print(answ)
