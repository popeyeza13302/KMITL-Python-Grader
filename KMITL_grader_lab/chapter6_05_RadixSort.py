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
                s += '->'
            p = p.next
        return s

    def size(self):
        count = 0
        p = self.head.next
        while p is not None:
            count += 1
            p = p.next
        return count

    def isEmpty(self):
        return self.size() == 0

    def nodeAt(self, index):    # -1 is dummy , 0 is first index
        p = self.head           # dummy head
        for _ in range(-1, index):
            p = p.next
        return p

    def insert(self, index, data):
        prevNode = self.nodeAt(index-1)
        newNode = Node(data, prevNode.next)
        prevNode.next = newNode

    def append(self, data):
        self.insert(self.size(), data)

    def pop(self, index):
        if self.isEmpty():             # check for case prevNode.next == None
            return 'No more to pop'
        if index > self.size()-1:
            return 'out of range'

        prevNode = self.nodeAt(index-1)
        nextNode = prevNode.next.next   # no case None.next / but nextNode can be None
        popNode = prevNode.next         # store popNode
        prevNode.next = nextNode
        return popNode  # return None or Node


# 64 8 216 512 27 729 0 1 343 12

inp = [int(i) for i in input('Enter Input : ').split()]

time = 0

L = SinglyLinkedList()

for i in inp:
    L.append(i)

print(time, 'Time(s)')
print('Before Radix Sort : ', L)
print('After  Radix Sort : ', None)

