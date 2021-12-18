data = open('etc/in').read().splitlines()[0].split(',')
data[0] = data[0][15:].split('..')
data[1] = data[1][3:].split('..')

x_bound = [int(x) for x in data[0]]
y_bound = [int(x) for x in data[1]]


# bruteforce xd

besty=0
start = (0,0)
for y_speed in range(1,1000):
    for x_speed in range(1,x_bound[1]):
        px,py = start
        sx,sy = x_speed,y_speed
        max_y=0
        for steps in range(0,500):
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
                if max_y > besty:
                    besty=max_y
                break

print(besty)
