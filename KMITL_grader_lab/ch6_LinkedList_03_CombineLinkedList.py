# week 6
# class Node
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return str(self.data)


class DoublyLinkedList:
    def __init__(self):
        self.head = Node(None, None, None)
        self.tail = Node(None, None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    def __str__(self):
        return self.forward()

    def forward(self):
        s = ''
        p = self.head.next
        while p != self.tail:
            s += str(p.data) + ' '
            p = p.next
        return s

    def reverse(self):
        s = ''
        p = self.tail.prev
        while p != self.head:
            s += str(p.data) + ' '
            p = p.prev
        return s

    def size(self):
        count = 0
        p = self.head.next
        while p != self.tail:
            count += 1
            p = p.next
        return count

    def nodeAt(self, index):
        p = self.head
        for _ in range(-1, index):
            p = p.next
        return p

    def append(self, data):
        self.insert(self.size(), data)

    def insert(self, index, data):
        # store node
        prevNode = self.nodeAt(index - 1)

        newNode = Node(data, prevNode, prevNode.next)
        prevNode.next = newNode.next.prev = newNode

def mergeLinked(firstLink, lastLink):
    newLinked = ''
    newLinked = firstLink.forward() + lastLink.reverse()
    return newLinked


inp = input('Enter Input (L1,L2) : ').split()

L1 = DoublyLinkedList()
L2 = DoublyLinkedList()

# I->Love->KMITL Datastruct->and

for i in range(len(inp)):
    inp[i] = inp[i].split('->')

for j in inp[0]:
    L1.append(j)
for j in inp[1]:
    L2.append(j)

print('L1    :', L1)
print('L2    :', L2)
print('Merge :', mergeLinked(L1, L2))
