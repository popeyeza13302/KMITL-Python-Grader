# class Node
class Node:
    def __int__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


class LinkedList:
    def __init__(self):
        self.head = Node(None, None)

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


# 64 8 216 512 27 729 0 1 343 125

inp = [int(i) for i in input('Enter Input : ').split()]

time = 0


print(time, 'Time(s)')
print('Before Radix Sort : ', None)
print('After  Radix Sort : ', None)

