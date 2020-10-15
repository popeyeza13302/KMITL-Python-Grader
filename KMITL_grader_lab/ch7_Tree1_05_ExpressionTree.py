class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

    def inOrder(self, node):
        if node is None:
            return
        if node.left is not None:   # not left leaf
            print('(', end='')
        self.inOrder(node.left)
        print(node, end='')
        self.inOrder(node.right)
        if node.right is not None:  # not right leaf
            print(')', end='')

    def preOrder(self, node):
        if node is None:
            return
        print(node, end='')
        self.preOrder(node.left)
        self.preOrder(node.right)


class Stack:
    def __init__(self):
        self.item = []

    def __str__(self):
        s = ''
        for i in self.item:
            s += str(i) + ' '
        return s

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.size() == 0

    def push(self, data):
        self.item.append(data)

    def pop(self, index=-1):
        return self.item.pop(index)


inp = [str(i) for i in input('Enter Postfix : ')]

tree = BinarySearchTree()

s = Stack()
for i in inp:
    if i in '+-*/':
        s.push(Node(i, s.pop(-2), s.pop()))     # left-right //pop first go right // pop second go left
    else:
        s.push(Node(i))

root = s.pop()
print('Tree : ')
tree.printTree(root)
print('--------------------------------------------------')
print('Infix : ', end='')
tree.inOrder(root)
print('\nPrefix : ', end='')
tree.preOrder(root)