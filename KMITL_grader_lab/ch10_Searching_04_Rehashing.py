class hash:
    def __init__(self, size, maxCol, thres):
        self.lst = [None] * size
        self.storeData = []             # store data in list
        self.maxCol = maxCol
        self.thres = thres
        self.tableSize = size
        self.realSize = 0

        print('Initial Table :')
        self.printTable()

    def printTable(self):
        for i in range(self.tableSize):
            print(f'#{i+1}\t{self.lst[i]}')
        print('----------------------------------------')

    def loadFactor(self):
        return self.realSize / self.tableSize * 100     # percent (*100)

    def insert(self, value):
        if value not in self.storeData:
            print(f'Add : {value}')         # add only new value
            self.storeData.append(value)    # stored only new value in list

        indexFirst = value % self.tableSize
        isMaxCol = False

        for n in range(maxCollision):
            index = (indexFirst + n**2) % self.tableSize        # quadratic probing
            if self.lst[index] is not None:
                print(f'collision number {n+1} at {index}')     # collision !
            else:
                self.lst[index] = value                         # found free space !
                self.realSize += 1
                break
        else:
            isMaxCol = True                                     # max collision

        # check is it need to rehash ?
        if self.loadFactor() > self.thres:  # case 1
            print('****** Data over threshold - Rehash !!! ******')
            self.rehash()
        elif isMaxCol is True:              # case 2
            print('****** Max collision - Rehash !!! ******')
            self.rehash()


    def rehash(self):
        self.tableSize = self.greaterPrimeNum()     # newTable Size
        self.lst = [None] * self.tableSize          # reset Table
        self.realSize = 0                           # reset Size

        for i in self.storeData:   # re-insert
            self.insert(i)

    def greaterPrimeNum(self):
        newPrime = self.tableSize * 2       # 2 times
        while True:
            isPrime = False
            for i in range(2, newPrime):    # check every num...
                if newPrime % i == 0:
                    break
            else:
                isPrime = True              # if check every num and only for 1 and its own num

            if isPrime is True:             # if prime .. break out
                break
            else:
                newPrime += 1               # go on to next prime...

        return newPrime                     # return newPrime



print(' ***** Rehashing *****')
require, inputlst = input('Enter Input : ').split('/')

require = list(map(int, require.split()))
tableSize, maxCollision, threshold = require[0], require[1], require[2]
inputlst = list(map(int, inputlst.split()))

hashTable = hash(tableSize, maxCollision, threshold)
for i in inputlst:
    hashTable.insert(i)
    hashTable.printTable()      # print everytime after insert