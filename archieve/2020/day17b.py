import copy

def simulate_cycle(cube):
    ans = copy.deepcopy(cube)

    # <#>:=active
    # <.>:=inactive
    for z in range(1,len(cube)-1):
        for y in range(1,len(cube[z])-1):
            for x in range(1,len(cube[z][y])-1):
                for w in range(1, len(cube[z][y][x])-1):
                    ctr=0
                    # bruteforce xd
                    #print("---checking ({},{},{}):\n".format(z,y,x))
                    for i in range(3):
                        for j in range(3):
                            for k in range(3):
                                for l in range(3):
                                    #print("({},{},{})..".format(z+(-1+i),y+(-1+j),x+(-1+k)), end=' ')
                                    #print(z+(-1+i),y+(-1+j),x+(-1+k),w+(-1+l))
                                    if cube[z+(-1+i)][y+(-1+j)][x+(-1+k)][w+(-1+l)] == '#':
                                        #print(" ..yes") 
                                        ctr+=1
                                    else:
                                        #print(" ..no") 
                                        5
                    
                    if cube[z][y][x][w] == '#':
                        ctr-=1
                        if not (ctr == 2 or ctr == 3):
                            ans[z][y][x][w] = '.'
                    else:
                        if ctr == 3:
                            ans[z][y][x][w] = '#'
                            if cube[z][y][x][w] == '#':
                                print("wtf?")
                                exit(0)
                #if ctr > 0:
                #    print("-------------({},{},{}) has {} neighbours.".format(z,y,x, ctr))

    return ans


def print_cube(cube):
    for z in range(len(cube)):
        print("z: {}".format(z))
        for y in range(len(cube[z])):
            for x in range(len(cube[z][y])):
                for w in range(len(cube[z][y][x])):
                    print(cube[z][y][x], end='')
            print()


def count_alive(cube):
    ctr=0
    for i in cube:
        for j in i:
            for k in j:
                for l in k:
                    if l == '#':
                        ctr += 1

    return ctr

def main():
    inp = open('etc/data.txt').read().splitlines()

    z_dim = 35
    y_dim = 35
    x_dim = 35
    w_dim = 35

    intial_surface = copy.deepcopy(inp)

    new_surface = []
    new_surface.clear()


    for y in range(len(intial_surface)):
        new_surface.append([])
        for x in range(len(intial_surface[y])):
            tmp = []
            tmp.append(intial_surface[y][x])
            for i in range(1,len(intial_surface)):
                tmp.append('.')
            #print(tmp)
            new_surface[y].append(tmp)

        


    cube=[]
    cube.clear()
    for i in range(z_dim):
        cube.append([])
        for j in range(y_dim):
            cube[i].append([])
            for k in range(x_dim):
                cube[i][j].append([])
                for l in range(w_dim):
                    cube[i][j][k].append('.')

    #print(cube[0][0][0][0])
    #print(new_surface[0][0][3])

    for y in range(len(new_surface)):
        for x in range(len(new_surface[y])):
            for w in range(len(new_surface[y][x])):
                cube[int(z_dim/2)][int(y_dim/2)+y][int(x_dim/2)+x][int(w_dim/2)+w] = new_surface[y][x][w]


    print(count_alive(cube))
    for i in range(6):
        print("cycle: {}".format(i))
        cube = simulate_cycle(cube)
        print(count_alive(cube))
        #print_cube(cube)
    

main()
