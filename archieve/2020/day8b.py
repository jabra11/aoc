
acc = 0

def main():
    opcodes = open('etc/data.txt').read().splitlines()

    for i in range(len(opcodes)):

        print(i)

        opcode = opcodes[i][0:3]
        cpy = opcodes.copy()

        # try bruteforcing nops first
        #if opcode == 'nop':
        #    cpy[i] = 'jmp' + cpy[i][3:]
        #    print("try insertion of {} at {}".format(cpy[i], i))

        #    good = brute_force_path(cpy)
        #    if good:
        #        print("worked!")
        #        break
        #    else:
        #        print("bad")

        if opcode == 'jmp':
            cpy[i] = 'nop' + cpy[i][3:]
            print("try insertion of {} at {}".format(cpy[i], i))

            good = brute_force_path(cpy)
            if good:
                print("worked!")
                break
            else:
                print("bad")

    print('acc: {}'.format(acc))


def brute_force_path(opcodes):
    i = 0
    acc = 0
    log = {}

    while i < len(opcodes):

        if i in log:
            log[i] += 1
            if log[i] == 3:
                return False

        else:
            log[i] = 1

        opcode = opcodes[i][0:3]
        arg = int(opcodes[i][5:]) 

        print("executing {}".format(opcodes[i]))

        if opcodes[i][4] == '-':
            arg = arg * -1

        if opcode == 'nop':
            i+=1

        elif opcode == 'jmp':
            i += arg
            
        elif opcode == 'acc':
            acc += arg
            i +=1

    print(acc)
    return True
    

main()
