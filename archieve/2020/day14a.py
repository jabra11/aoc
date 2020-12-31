def main():
    input = open('etc/data.txt').read().splitlines()

    cur_mask = ''
    
    map = {}
    for i in input:
        if i[:4] == 'mask':
            cur_mask = i[7:] 
        else:

            address = []
            j = 4
            while j < len(i):
                if i[j] != ']':
                    address.append(i[j])
                else:
                    break
                
                j +=1
            address = int("".join(address))

            value = int(i[j+4:])
            value = "{:b}".format(value).zfill(36)
            value = list(value)

            for i in range(len(cur_mask)):
                if cur_mask[i] == '0':
                    value[i] = '0'
                elif cur_mask[i] == '1':
                    value[i] = '1'
        
            value = int("".join(value), 2)
        
            map[address] = value

    sum=0
    for i in map:
        sum+=map[i]

    print(sum)
        

main()
