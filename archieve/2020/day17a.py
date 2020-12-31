import copy

def simulate_cycle(cube):
    ans = copy.deepcopy(cube)

    # <#>:=active
    # <.>:=inactive
    for z in range(1,len(cube)-1):
        for y in range(1,len(cube[z])-1):
            for x in range(1,len(cube[z][y])-1):
                ctr=0
                # bruteforce xd
                #print("---checking ({},{},{}):\n".format(z,y,x))
                for i in range(3):
                    for j in range(3):
                        for k in range(3):
                            #print("({},{},{})..".format(z+(-1+i),y+(-1+j),x+(-1+k)), end=' ')
                            if cube[z+(-1+i)][y+(-1+j)][x+(-1+k)] == '#':
                                #print(" ..yes") 
                                ctr+=1
                            else:
                                #print(" ..no") 
                                5
                
                if cube[z][y][x] == '#':
                    ctr-=1
                    if not (ctr == 2 or ctr == 3):
                        ans[z][y][x] = '.'
                else:
                    if ctr == 3:
                        ans[z][y][x] = '#'
                        if cube[z][y][x] == '#':
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
                print(cube[z][y][x], end='')
            print()


def count_alive(cube):
    ctr=0
    for i in cube:
        for j in i:
            for k in j:
                if k == '#':
                    ctr += 1

    return ctr

def main():
    inp = open('etc/data.txt').read().splitlines()

    intial_surface = inp
    # [z[y[x]]]

    z_dim = 50
    y_dim = 50
    x_dim = 50

    cube=[[[[]]]]
    cube.clear()
    for i in range(z_dim):
        cube.append([])
        for j in range(y_dim):
            cube[i].append([])
            for k in range(x_dim):
                cube[i][j].append('.')

    

    for y in range(len(intial_surface)):
        for x in range(len(intial_surface[y])):
            cube[int(z_dim/2)][int(y_dim/2) + y][int(x_dim/2)+x] = intial_surface[y][x]



    print_cube(cube)

    for i in range(6):
        print("cycle: {}".format(i))
        cube = simulate_cycle(cube)
        print_cube(cube)
    
    print(count_alive(cube))
main()
