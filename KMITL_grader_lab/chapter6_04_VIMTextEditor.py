# class Node
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.cursorNode = Node('|', None)
        self.head.next = self.cursorNode

    def __str__(self):
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

    def beforeBeforeNode(self):
        p = self.head
        '''
        print('1',p)
        print('2',p.next)
        print('3',p.next.next)
        '''
        if p.next == self.cursorNode:  # case first [dummy]->[cursor]->None
            return None
        while p.next.next != self.cursorNode:
            p = p.next
        return p

    def beforeNode(self):
        p = self.head
        while p.next != self.cursorNode:
            p = p.next
        return p

    def afterNode(self):
        return self.cursorNode.next

    def afterAfterNode(self):
        if self.cursorNode.next is None or self.cursorNode.next.next is None:
            return None
        return self.cursorNode.next.next

    def insertBefore(self, data):
        newNode = Node(data, self.cursorNode)
        self.beforeNode().next = newNode

    def insertAfter(self, data):
        newNode = Node(data, self.cursorNode.next)
        self.cursorNode.next = newNode

    def append(self, data):  # normal case insert before cursor
        self.insertBefore(data)

    def deleteLeft(self):
        self.popLeft()

    def deleteRight(self):
        self.popRight()

    def popLeft(self):
        prevNode = self.beforeBeforeNode()
        if prevNode is None:
            popNode = None
            self.head.next = self.cursorNode  # No more to delete
        else:
            popNode = prevNode.next
            prevNode.next = self.cursorNode
        return popNode

    def popRight(self):
        if self.cursorNode.next is None:
            popNode = None
        else:
            popNode = self.cursorNode.next
            self.cursorNode.next = self.afterAfterNode()
        return popNode

    def shiftLeft(self):
        popNode = self.popLeft()
        if popNode is not None:  # No more to shift
            self.insertAfter(popNode.data)

    def shiftRight(self):
        popNode = self.popRight()
        if popNode is not None:
            self.insertBefore(popNode.data)


# I A,I B,I C,I D,I E,I G,L,L,L,L,D
inp = input('Enter Input : ').split(',')

L = SinglyLinkedList()

for i in inp:
    i = i.split()
    if i[0] == 'I':
        L.append(i[1])
    elif i[0] == 'L':
        L.shiftLeft()
    elif i[0] == 'R':
        L.shiftRight()
    elif i[0] == 'B':
        L.deleteLeft()
    elif i[0] == 'D':
        L.deleteRight()

print(L)
