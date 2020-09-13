class Node:
    def __init__(self, value, next_node=None, prev_node=None):
        self.value = value
        self.next_node = next_node
        self.prev_node = prev_node

    def __str__(self):
        return str(self.value)

"""
BASIC
size()  # variable/loop
element_at(pos)/node_at(pos)

is_empty()

push_back(value)  # queue push
push_front(value)  # stack push
pop_back()  # stack pop
pop_front()  # queue pop

ADVANCE
insert(pos, value)
pop(pos, value)
remove(value) + index_of(value)
"""

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def size(self):
        curr = self.head
        count = 0
        while curr is not None:
            count += 1
            curr = curr.next_node
        return count

    def node_at(self, pos):
        if 0 <= pos < self.size():
            curr = self.head
            count = 0
            while curr is not None:
                if count == pos:
                    break
                count += 1
                curr = curr.next_node
            return curr
        else:
            print('Index out of bound')
            return

    def value_at(self, pos):
        temp = self.node_at(pos)
        if temp is not None:
            return temp.value
        return

    def is_empty(self):
        return self.head is None

    def push_back(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, prev_node=self.tail)
            self.tail.next_node = new_node
            self.tail = new_node

    def push_front(self, value):
        if self.is_empty():
            self.head = self.tail = Node(value)
        else:
            new_node = Node(value, self.head)
            self.head.prev_node = new_node
            self.head = new_node

    def pop_back(self):
        if self.is_empty():
            print("Can't pop_back: empty list")
            return -1
        else:
            value = self.tail.value
            prev = self.tail.prev_node
            self.tail.prev_node = None
            self.tail = prev
            if prev is not None:
                prev.next_node = None
            else:
                self.head = self.tail = None
            return value

    def pop_front(self):
        if self.is_empty():
            print("Can't pop_front: empty list")
            return -1
        else:
            value = self.head.value
            next_node = self.head.next_node
            self.head.next_node = None
            self.head = next_node
            if next_node is not None:
                next_node.prev_node = None
            else:
                self.head = self.tail = None
            return value

    def insert(self, pos, value):
        if pos == 0 or self.is_empty():
            self.push_front(value)
        elif pos >= self.size():
            self.push_back(value)
        elif pos < 0:  # insert from back (index of self.tail.prev_node = -1)
            pos = self.size()+pos
            if pos <= 0:
                self.push_front(value)
            else:
                curr = self.node_at(pos)
                prev = curr.prev_node
                new_node = Node(value, curr, prev)
                prev.next_node = new_node
                curr.prev_node = new_node
        else:
            curr = self.node_at(pos)
            prev = curr.prev_node
            new_node = Node(value, curr, prev)
            prev.next_node = new_node
            curr.prev_node = new_node

    def pop(self, pos):
        if self.is_empty():
            print("Can't pop: list is empty")
            return
        elif pos == 0:
            return self.pop_front()
        elif pos == self.size()-1:
            return self.pop_back()
        elif 0 <= pos < self.size():
            curr = self.node_at(pos)
            prev_node = curr.prev_node
            next_node = curr.next_node
            prev_node.next_node = next_node
            next_node.prev_node = prev_node
            curr.prev_node = None
            curr.next_node = None
            return curr.value

    def index_of(self, value):
        curr = self.head
        count = 0
        while curr is not None:
            if curr.value == value:
                return count
            curr = curr.next_node
            count += 1
        return -1

    def remove(self, value):
        pos = self.index_of(value)
        if pos != -1:
            if pos == 0:
                self.pop_front()
            elif pos == self.size()-1:
                self.pop_back()
            else:
                self.pop(pos)
        else:
            print("Empty list or no such value")
            return

    def __str__(self):
        lst = []
        curr = self.head
        while curr is not None:
            lst.append(curr.value)
            curr = curr.next_node
        return str(lst)


if __name__ == '__main__':
    ll = DoublyLinkedList()
    ll.insert(555, 0.5)
    ll.push_front(-1)
    ll.push_front(-2)
    ll.push_front(-3)
    ll.push_front(-4)
    ll.push_front(-5)
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)
    ll.insert(5, 0)
    ll.insert(-999, -6)
    ll.insert(999, 6)
    print(ll)
    while not ll.is_empty():
        print(ll.pop_back())
    ll.pop_back()

    ll.insert(555, 0.5)
    ll.push_front(-1)
    ll.push_front(-2)
    ll.push_front(-3)
    ll.push_front(-4)
    ll.push_front(-5)
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)
    ll.insert(5, 0)
    ll.insert(-999, -6)
    ll.insert(999, 6)
    while not ll.is_empty():
        print(ll.pop_front())
    ll.pop_front()

    ll.pop(0)
    ll.insert(555, 0.5)
    ll.push_front(-1)
    ll.push_front(-2)
    ll.push_front(-3)
    ll.push_front(-4)
    ll.push_front(-5)
    ll.push_back(1)
    ll.push_back(2)
    ll.push_back(3)
    ll.push_back(4)
    ll.push_back(5)
    ll.insert(5, 0)
    ll.insert(-999, -6)
    ll.insert(999, 6)
    print(ll.pop(0))
    print(ll.pop(ll.size()-1))
    print(ll.pop(ll.size()//2))
    print(ll)
    ll.remove(-5)
    print(ll)
    ll.remove(5)
    print(ll)
    ll.remove(0)
    print(ll)
    while not ll.is_empty():
        ll.remove(ll.value_at(0))
        print(ll)
    ll.remove(4)
    print(ll)