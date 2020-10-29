# Cr. Qiral Github (dek here rach)

def printTree(n, level=0):
    if n > len(num)-1:
        return
    printTree(2 * n + 2, level + 1)
    print('        ' * level, num[n])
    printTree(2 * n + 1, level + 1)


k, dayList = input('Enter Input : ').split('/')
dayList = [int(i) for i in dayList.split()]

num = []
van = {}    # dict

for i in range(int(k)):
    num.append(i + 1)           # number of van
    van[i+1] = van.get(i+1, 0)  # set day to 0 of van  // .get(data, defaultNum)

for i in range(len(dayList)):
    #printTree(0)

    minNum = num.pop(0)
    van[minNum] = van.get(minNum, 0) + int(dayList[i])    # add day reserve by dayList[i]
    print(f'Customer {i+1} Booking Van {minNum} | {dayList[i]} day(s)')
    #print('--------------------------------------------------')

    for index in range(len(num)):   # run every index

        # day[0] < day[1,2,3,4,5,6,7,8...] // day[0] == day[1,2,3,4,5,6,7,8...] and minNum < number (same day..different number)
        if van[minNum] < van[num[index]] or (van[minNum] == van[num[index]] and minNum < num[index]):
            num.insert(index, minNum)  # sorted and insert min between list
            minNum = None
            break

    if minNum is not None:  # if can't insert and have minNum
        num.append(minNum)  # append last one to num

'''

k, dayInputList = input('Enter Input : ').split('/')
dayInputList = [int(i) for i in dayInputList.split()]

k = int(k)

num = []
day = []

for i in range(k):
    num.append(i + 1)
    day.append(0)


# tree.node = tree.insert(0, numberList)

def insertSort(n, amountDay):
    if n == 0:
        day[0] += amountDay

    elif 2*n+1 > len(num) - 1:  # base case 1
        return
    elif 2*n+2 > len(num) - 1:  # base case 2
        return

    if day[n] >= day[2*n+2]:  # more than or equal right
        day[n], day[2*n+2] = day[2*n+2], day[n]     # swap right
        num[n], num[2*n+2] = num[2*n+2], num[n]     # swap right

        insertSort(2*n+2, amountDay)    # recursion go inside right

    else:                   # less than right
        day[n], day[2*n+1] = day[2*n+1], day[n]     # swap left
        num[n], num[2*n+1] = num[2*n+1], num[n]     # swap left

        insertSort(2*n+1, amountDay)    # recursion go inside left


def reArrange(n):
    if 2*n+1 > len(num) - 1:
        return
    elif 2*n+2 > len(num) - 1:
        return

    if day[n] == day[2*n+1]:
        if num[n] > num[2*n+1]:
            day[n], day[2*n+1] = day[2*n+1], day[n]  # swap left
            num[n], num[2*n+1] = num[2*n+1], num[n]  # swap left
            reArrange(2*n+1)

    elif day[n] == day[2*n+2]:
        if num[n] > num[2*n+2]:
            day[n], day[2*n+2] = day[2*n+2], day[n]  # swap right
            num[n], num[2*n+2] = num[2*n+2], num[n]  # swap right
            reArrange(2*n+2)

    if day[n] > day[2*n+1]:
        day[n], day[2*n+1] = day[2*n+1], day[n]  # swap left
        num[n], num[2*n+1] = num[2*n+1], num[n]  # swap left cause left always has lowest day
        reArrange(2*n+1)


def printTree(n, level=0):
    if n > len(num)-1:
        return

    printTree(2*n+2, level+1)
    print('        '*level, num[n])
    printTree(2*n+1, level+1)


def extractMin(n):
    if n == 0:
        min = num[0]
        num[0] = num[-1]
        day[0] = day[-1]

    if 2*n+1 > len(num):
        pass


    return min

for i in range(len(dayInputList)):
    position = num[0]# extractMin()
    printTree(0)
    insertSort(0, dayInputList[i])
    reArrange(0)

    print(f'Customer {i + 1} Booking Van {position} | {dayInputList[i]} day(s)')


'''

    # below are wrong code direction... I can't do in tree... I'm doing in Array and print as Tree :)


'''
    def insert(self, n, lst):

        if n >= k:
            return None
        currentNode = Node(lst[n])
        currentNode.left = self.insert(2 * n + 1, lst)
        currentNode.right = self.insert(2 * n + 2, lst)

        return currentNode

    def printTree(self, node, level=0):
        if node is None:
            return

        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

    def swapRootMin(self):
        lastNode = None
        currentNode = self.node
        while lastNode is None:
            if currentNode.right is not None:
                currentNode = currentNode.right
            elif currentNode.left is not None:
                currentNode = currentNode.left
            else:
                lastNode = currentNode      # get last Node (nothing to right and left)

        lastNode.data, self.node.data = self.node.data, lastNode.data   # SWAP!!!!

        print(self.node, ':',lastNode)

'''




'''
if dayList[n] > dayList[2*n+1] or dayList[n] > dayList[2*n+2]:  # if left or right less day than parent
    if dayList[2*n+1] > dayList[2*n+2]: # left day > right day
        numberList[n], numberList[2*n+2] = numberList[2*n+2], numberList[n]  # swap less data(right) to parent
        dayList[n], dayList[2*n+2] = dayList[2*n+2], dayList[n]  # swap less data(right) to parent
        minHeapArray(2*n+2, amountDay)  # recursion right...

    elif dayList[2*n+1] < dayList[2*n+2]:   # left day < right day
        print('tttt')

        numberList[n], numberList[2*n+1] = numberList[2*n+1], numberList[n]  # swap less data(left) to parent
        dayList[n], dayList[2*n+1] = dayList[2*n+1], dayList[n]  # swap less data(left) to parent
        print('numberList', numberList)
        print('dayList', dayList)
        minHeapArray(2*n+1, amountDay)  # recursion left...


elif dayList[n] == dayList[2*n+1] and dayList[n] == dayList[2*n+2]: # if left and right more than equal day to parent
    if numberList[2*n+1] > numberList[2*n+2]:   # left num > right num
        numberList[n], numberList[2*n+2] = numberList[2*n+2], numberList[n]  # swap less data(right) to parent
        dayList[n], dayList[2*n+2] = dayList[2*n+2], dayList[n]  # swap less data(right) to parent
        minHeapArray(2*n+2, amountDay)   # recursion right...

    elif numberList[2*n+1] < numberList[2*n+2]: # left num < right num
        numberList[n], numberList[2*n+1] = numberList[2*n+1], numberList[n]  # swap less data(left) to parent
        dayList[n], dayList[2*n+1] = dayList[2*n+1], dayList[n]  # swap less data(left) to parent
        minHeapArray(2*n+1, amountDay)  # recursion left...

elif dayList[n] == dayList[2*n+1]:  # if parent day == left day
    numberList[n], numberList[2*n+1] = numberList[2*n+1], numberList[n]  # swap less data(left) to parent
    dayList[n], dayList[2*n+1] = dayList[2*n+1], dayList[n]  # swap less data(left) to parent
    minHeapArray(2*n+1, amountDay)  # recursion left...

elif dayList[n] == dayList[2*n+2]:  # if parent day == right day
    numberList[n], numberList[2*n+2] = numberList[2*n+2], numberList[n]  # swap less data(right) to parent
    dayList[n], dayList[2*n+2] = dayList[2*n+2], dayList[n]  # swap less data(right) to parent
    minHeapArray(2*n+2, amountDay)  # recursion right...


'''