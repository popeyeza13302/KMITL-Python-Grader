# week 6
# class Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None, None)

    def __str__(self):
        s = ''
        p = self.head.next
        while p is not None:
            s += str(p.data)
            if p.next is not None:
                s += ' -> '
            p = p.next
        return s

    def display(self):
        s = ''
        p = self.head.next
        while p is not None:
            s += str(p.data) + ' '
            p = p.next
        return s

    def size(self):
        count = 0
        p = self.head.next
        while p is not None:
            count += 1
            p = p.next
        return count

    def checkMaxAndInsert(self, newValue):
        p = self.head.next
        for index in range(self.size()):
            if newValue > p.data:
                self.insert(index, newValue)
                return
            p = p.next
        else:
            self.append(newValue)

    def isEmpty(self):
        return self.size() == 0

    def nodeAt(self, index):  # -1 is dummy , 0 is first index
        p = self.head  # dummy head
        for _ in range(-1, index):
            p = p.next
        return p

    def insert(self, index, data):
        prevNode = self.nodeAt(index - 1)
        newNode = Node(data, prevNode.next)
        prevNode.next = newNode

    def append(self, data):
        self.insert(self.size(), data)

    def pop(self, index):
        if self.isEmpty():  # check for case prevNode.next == None
            return 'No more to pop'
        if index > self.size() - 1:
            return 'out of range'

        prevNode = self.nodeAt(index - 1)
        nextNode = prevNode.next.next  # no case None.next / but nextNode can be None
        popNode = prevNode.next  # store popNode
        prevNode.next = nextNode
        return popNode  # return None or Node

# CAUTION! this is not a real radixSort...
# it's sort inside it's own data.
def radixSort(linkedList):
    state = False
    time = 0
    size = linkedList.size()
    zeroLinked = SinglyLinkedList()     # I lazy to optimize code to array :P
    oneLinked = SinglyLinkedList()      # make sure that programming has no bug for first time test
    twoLinked = SinglyLinkedList()
    threeLinked = SinglyLinkedList()
    fourLinked = SinglyLinkedList()
    fiveLinked = SinglyLinkedList()
    sixLinked = SinglyLinkedList()
    sevenLinked = SinglyLinkedList()
    eightLinked = SinglyLinkedList()
    nightLinked = SinglyLinkedList()

    for digit in range(1000):  # digit ones->tens->hundreds->...
        for _ in range(size):  # size of LinkedList
            popNode = linkedList.pop(0)

            originalData = popNode.data
            if originalData >= 0:
                calculatedData = originalData // 10 ** digit
            else:
                calculatedData = -originalData // 10 ** digit

            if calculatedData % 10 == 0:
                zeroLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 1:
                oneLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 2:
                twoLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 3:
                threeLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 4:
                fourLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 5:
                fiveLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 6:
                sixLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 7:
                sevenLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 8:
                eightLinked.checkMaxAndInsert(originalData)
            elif calculatedData % 10 == 9:
                nightLinked.checkMaxAndInsert(originalData)

        print('------------------------------------------------------------')
        print('Round :', digit + 1)
        print('0 :', zeroLinked.display())
        print('1 :', oneLinked.display())
        print('2 :', twoLinked.display())
        print('3 :', threeLinked.display())
        print('4 :', fourLinked.display())
        print('5 :', fiveLinked.display())
        print('6 :', sixLinked.display())
        print('7 :', sevenLinked.display())
        print('8 :', eightLinked.display())
        print('9 :', nightLinked.display())

        if not zeroLinked.isEmpty() and oneLinked.isEmpty() and twoLinked.isEmpty() and \
                threeLinked.isEmpty() and fourLinked.isEmpty() and fiveLinked.isEmpty() and \
                sixLinked.isEmpty() and sevenLinked.isEmpty() and eightLinked.isEmpty() and nightLinked.isEmpty():
            state = True

        # return back to linkedlist
        while not zeroLinked.isEmpty(): linkedList.append(zeroLinked.pop(0).data)
        while not oneLinked.isEmpty(): linkedList.append(oneLinked.pop(0).data)
        while not twoLinked.isEmpty(): linkedList.append(twoLinked.pop(0).data)
        while not threeLinked.isEmpty(): linkedList.append(threeLinked.pop(0).data)
        while not fourLinked.isEmpty(): linkedList.append(fourLinked.pop(0).data)
        while not fiveLinked.isEmpty(): linkedList.append(fiveLinked.pop(0).data)
        while not sixLinked.isEmpty(): linkedList.append(sixLinked.pop(0).data)
        while not sevenLinked.isEmpty(): linkedList.append(sevenLinked.pop(0).data)
        while not eightLinked.isEmpty(): linkedList.append(eightLinked.pop(0).data)
        while not nightLinked.isEmpty(): linkedList.append(nightLinked.pop(0).data)

        if state is True:
            break
        time += 1
    return linkedList, time


# 64 8 216 512 27 729 0 1 343 125

inp = [int(i) for i in input('Enter Input : ').split()]

L = SinglyLinkedList()
L_Origin = SinglyLinkedList()

for i in inp:
    L.append(i)
    L_Origin.append(i)

time = 0
radixLinked, time = radixSort(L)
print('------------------------------------------------------------')
print(time, 'Time(s)')
print('Before Radix Sort :', L_Origin)
print('After  Radix Sort :', radixLinked)
