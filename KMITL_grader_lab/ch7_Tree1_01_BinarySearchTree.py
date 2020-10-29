class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = Node(data)  # store new Node
        if self.root is None:  # first case
            self.root = newNode
        else:  # others case
            currentNode = self.root
            while True:
                if data > currentNode.data:  # add right branch
                    if currentNode.right is None:  # if case bottom right
                        currentNode.right = newNode  # assign right
                        break
                    currentNode = currentNode.right  # point to next node

                elif data < currentNode.data:  # add left branch
                    if currentNode.left is None:  # if case bottom left
                        currentNode.left = newNode  # assign left
                        break
                    currentNode = currentNode.left  # point to next node

        return self.root  # always return node

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node.data)
        self.printTree(node.left, level + 1)


inp = [int(i) for i in input('Enter Input : ').split()]

tree = BinarySearchTree()

for i in inp:
    root = tree.insert(i)

tree.printTree(root)

