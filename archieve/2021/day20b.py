import sys; datafilepath = sys.argv[1]
raw_data = open(datafilepath).read().splitlines()

alg = raw_data[0]

inp = list(list())

for i in raw_data[2:]:
    inp.append(i)

import copy

for run in range(50):
    length = 750
    offset = length//2
    output = list(list())


    fil = ''
    if run % 2 == 0:
        fil = '.'
    else:
        fil = '#'

    for i in range(length):
        tmp = list()
        for j in range(length):
            tmp.append(fil)
        output.append(tmp)

    framed_inp = list(list())
    framed_inp.append([fil] * (len(inp)+6))
    framed_inp.append([fil] * (len(inp)+6))
    framed_inp.append([fil] * (len(inp)+6))
    for i in inp:
        framed_inp.append([fil,fil,fil] + list(i) + [fil,fil,fil])
    framed_inp.append([fil] * (len(inp)+6))
    framed_inp.append([fil] * (len(inp)+6))
    framed_inp.append([fil] * (len(inp)+6))


    for i in range(len(inp)):
        for j in range(len(inp[i])):
            framed_inp[i+3][j+3] = inp[i][j]

    for y in range(1,len(framed_inp)-1):
        for x in range(1,len(framed_inp[y])-1):
            idx=list()
            for i in [-1,0,1]:
                for j in [-1,0,1]:
                    idx.append(framed_inp[y+i][x+j])
            for i in range(len(idx)):
                if idx[i] == '#':
                    idx[i] = '1'
                else:
                    idx[i] = '0'
            idx = "".join(idx)
            output[y+offset][x+offset] = alg[int(idx,2)]



    # shave output


    to_shave = ''
    if fil == '#':
        to_shave = '.'
    else:
        to_shave = '#'

    shaved_output = list(list())
    for i in output:
        if to_shave in i:
            shaved_output.append(i)
            continue

    left_min=9999999999999
    for i in output:
        for j in range(len(i)):
            if i[j] == to_shave:
                if j-1 < left_min:
                    left_min = j


    right_min=9999999999999
    for i in output:
        for j in range(len(i)-1, 0, -1):
            if i[j] == to_shave:
                if len(i)-(j) < right_min:
                    right_min = len(i)-(j-1)

    for i in range(len(shaved_output)):
        shaved_output[i] = shaved_output[i][left_min:len(shaved_output[i])-right_min+2]

    inp = shaved_output

sum = 0
for i in inp:
    sum += i.count('#')
print(sum)
