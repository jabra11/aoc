import math
import itertools

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

            address = "{:b}".format(address).zfill(36)
            address = list(address)

            for i in range(len(cur_mask)):
                if cur_mask[i] == '1':
                    address[i] = '1'
                elif cur_mask[i] == 'X':
                    address[i] = 'X'
            
            perm = []
            for i in address:
                if i == 'X':
                    perm.append('0')

            count_perm = 2**len(perm)
            print("{} possible perms for address {}:".format(count_perm, "".join(address)))

            new_address = address.copy()
            j=0
            for i in range(len(new_address)):
                if new_address[i] == 'X':
                    new_address[i] = perm[j]
                    j+=1
            
            a = int("".join(new_address), 2)
            map[a] = value
            print("{:b}".format(a).zfill(36))

            for i in range(count_perm-1):

                new_perm = int("".join(perm.copy()),2)
                new_perm += 1
                new_perm = "{:b}".format(new_perm).zfill(len(perm))
                new_perm = list(new_perm)

                new_address = address.copy()
                j=0
                for i in range(len(new_address)):
                    if new_address[i] == 'X':
                        new_address[i] = new_perm[j]
                        j+=1
                
                a = int("".join(new_address), 2)
                print("{:b}".format(a).zfill(36))
                map[a] = value
                perm = new_perm

    sum=0
    for i in map:
        sum+=map[i]
    print(sum)
        
main()
