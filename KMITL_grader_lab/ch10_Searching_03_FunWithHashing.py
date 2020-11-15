class Data:
    def __init__(self, key, value):     # like a dict() with homemade class
        self.key = key
        self.value = value

    def __str__(self):
        return f'({self.key}, {self.value})'


class hash:
    def __init__(self, size, maxCol):
        self.lst = [None] * size        # lst of None (table size)
        self.maxCol = maxCol            # maxCollision
        self.tableSize = size           # table size
        self.realSize = 0               # init size (0)

    def printTable(self):
        for i in range(self.tableSize):         # print table size
            print(f'#{i+1}\t{self.lst[i]}')
        print('---------------------------')

    def insert(self, key, value):
        if self.realSize == self.tableSize:
            return False                    # table is full / cannot insert

        newData = Data(key, value)          # assign newData
        sum = 0
        for i in key:
            sum += ord(i)
        indexFirst = sum % self.tableSize   # find first index

        for n in range(self.maxCol):
            index = (indexFirst + n**2) % self.tableSize        # quadratic Probing +0 +1 +4 +9 ... n^2

            if self.lst[index] is not None:
                print(f'collision number {n+1} at {index}')     # collision with something...
            else:
                self.lst[index] = newData           # assign newData to table[index]
                self.realSize += 1                  # realSize++
                break                               # break out if already assign...
        else:
            print('Max of collisionChain')          # Max Collision

        return True     # can insert

# 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love

print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
tableSize, maxColis = map(int, inp[0].split())
lst = inp[1].split(',')

hashTable = hash(tableSize, maxColis)

for i in lst:
    i = i.split()
    canInsert = hashTable.insert(i[0], i[1])    # Insert .. and get can/cannot Insert

    if canInsert is True:                   # can insert .. print table
        hashTable.printTable()
    else:
        print('This table is full !!!!!!')  # cannot insert .. don't print table .. and break out!
        break
