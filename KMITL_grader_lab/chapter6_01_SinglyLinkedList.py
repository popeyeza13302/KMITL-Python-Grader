# week 6
# Node Class
class Node:
    def __init__(self, data, next=None):
        self.data = data
        if next is None:
            self.next = None
        else:
            self.next = next

    def __str__(self):
        return str(self.data) + ' ' + str(self.next)


class SinglyLinkedList:
    def __init__(self):
        self.head = Node(None, None)
        self.size = 0

    def __str__(self):
        s = 'link list : '
        p = self.head.next
        if self.isEmpty():
            return 'List is empty'
        while p is not None:
            s += str(p.data)
            if p.next is not None:
                s += '->'
            p = p.next
        return s

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def indexOf(self, data):
        q = self.head.next
        for i in range(len(self)):
            if q.data == data:
                return i
            q = q.next
        return -1

    def isIn(self, data):
        return self.indexOf(data) >= 0

    def nodeAt(self, index):
        p = self.head
        for _ in range(index+1):
            p = p.next
        return p

    def append(self, data):
        x = 1
        return self.insert(len(self), data, x)

    def insert(self, index, data, x):
        if index > len(self) or index < 0:
            print('Data cannot be added')
            return
        if x != 1:
            print('index =', index, 'and data =', data)
        prevNode = self.nodeAt(index - 1)
        newNode = Node(data, prevNode.next)
        prevNode.next = newNode

        # p.next = Node(data, p.next)   # shortcut
        self.size += 1

    '''
    def delete(self, data):
        if self.isIn(data):
            p = self.nodeAt(self.indexOf(data) - 1)
            p.next = p.next.next
            self.size -= 1
    '''


inp = input('Enter Input : ').split(',')

linklst = SinglyLinkedList()

for i in inp[0].split():
    linklst.append(i)

print(linklst)

for i in inp[1:]:
    i = i.split(':')
    linklst.insert(int(i[0]), i[1], 0)
    print(linklst)
