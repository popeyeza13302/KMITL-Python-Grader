class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data)

class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None,None)
        self.size = 0

    def __str__(self):
        s = ''
        p = self.head.next
        while p != None:
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def nodeAt(self, index):
        p = self.head
        for i in range(-1,index):
            p = p.next
        return p

    def insert(self, index, data):
        prevNode = self.nodeAt(index - 1)
        newNode = Node(data, prevNode.next)
        prevNode.next = newNode
        self.size += 1

    def append(self, data):
        self.insert(self.size, data)

    def pop(self, index):
        prevNode = self.nodeAt(index - 1)
        popNode = prevNode.next
        if popNode is None:
            return popNode
        else:
            prevNode.next = popNode.next
            self.size -= 1
            return popNode

    def popRight(self):
        self.pop(self.size-1)


linked = SinglyLinkedList()

linked.append(1)
linked.append(2)
linked.append(3)
linked.append(4)
linked.append(5)

print('linked:',linked)

linked.popRight()
linked.popRight()
linked.popRight()
print('linked:',linked)
linked.popRight()
linked.popRight()

print('linked:',linked)

