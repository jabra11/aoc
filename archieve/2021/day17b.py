data = open('etc/in').read().splitlines()[0].split(',')
data[0] = data[0][15:].split('..')
data[1] = data[1][3:].split('..')

x_bound = [int(x) for x in data[0]]
y_bound = [int(x) for x in data[1]]


# bruteforce xd

ctr=0
start = (0,0)
for y_speed in range(-2000,2000):
    for x_speed in range(0,x_bound[1]+100):
        px,py = start
        sx,sy = x_speed,y_speed
        max_y=0
        for steps in range(0,1000):
            px += sx
            py += sy

            if sy > 0:
                max_y = py
            if sx>0:
                sx-=1
            else:
                if px < x_bound[0]:
                    break
            if px > x_bound[1] or py < y_bound[0]:
                break
            sy-=1
            
            if px >= x_bound[0] and px <= x_bound[1] and py >= y_bound[0] and py <= y_bound[1]:
                ctr+=1
                break

print(ctr)
