
def main():
    opcodes = open('etc/data.txt').read().splitlines()

    acc = 0

    log = {}

    i = 0
    while i < len(opcodes):


        if i in log:
            print("acc: {}".format(acc))
            break
        else:
            log[i] = 0

        opcode = opcodes[i][0:3]


        if opcode == 'nop':
            i += 1

        elif opcode == 'jmp':
            offset = int(opcodes[i][5:]) 
            
            if opcodes[i][4] == '-':
                offset = offset * -1

            i += offset

            
        elif opcode == 'acc':
            val = int(opcodes[i][5:]) 
            if opcodes[i][4] == '-':
                val = val * -1
            acc += val
            i +=1
        

        

        


main()
