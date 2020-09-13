# Node Class
class Node:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        if prev is None:
            self.prev = None
        else:
            self.prev = prev
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return 'NODE : ' + str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        if self.isEmpty():
            return "Empty"
        s = ""
        p = self.head.next
        while p.next is not None:
            s += str(p.data) + " "
            p = p.next
        return s

    def reverse(self):
        if self.isEmpty():
            return "Empty"
        s = ""
        p = self.tail.prev
        while p.prev is not None:
            s += str(p.data) + " "
            p = p.prev
        return s

    def size(self):
        p = self.head.next
        count = 0
        while p != self.tail:
            count += 1
            p = p.next
        return count

    def isEmpty(self):
        return self.size() == 0

    def nodeAt(self, index):
        p = self.head
        for _ in range(-1, index):
            p = p.next
        return p        # return Node

    def append(self, data):
        self.insert(self.size(), data)

    def addHead(self, data):
        self.insert(0, data)

    def insert(self, index, data):
        # stored node
        currentNode = self.nodeAt(index-1)  # if index = 0 current node will be self.head
        # new node
        newNode = Node(data, currentNode,currentNode.next)
        currentNode.next = newNode.next.prev = newNode
        '''
        print('NOW', newNode.data)
        print('NEXT', newNode.next.data)
        print('PRE', newNode.prev.data)
        print('___')
        '''

    def search(self, data):
        p = self.head.next
        while p is not None:
            if p.data == data:
                return 'Found'
            p = p.next
        return 'Not Found'

    def indexOf(self, data):
        p = self.head.next
        for i in range(self.size()):
            if p.data == data:
                return i
            p = p.next
        return -1

    def pop(self, index):
        if not 0 <= index < self.size():
            return 'Out of Range'
        # store node
        currentNode = self.nodeAt(index)

        currentNode.prev.next = currentNode.next
        currentNode.next.prev = currentNode.prev

        return 'Success'

# AP I,AP Love,AP KMITL,AP 2020
L = DoublyLinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:], L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.size(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.indexOf(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
    elif i[:2] == "IS":
        data = i[3:].split()
        L.insert(int(data[0]), data[1])
print("Linked List :", L)
print("Linked List Reverse :", L.reverse())
