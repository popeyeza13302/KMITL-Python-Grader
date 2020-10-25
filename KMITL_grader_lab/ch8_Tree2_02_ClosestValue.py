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
        self.lst = []

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while currentNode is not None:
                if data > currentNode.data:
                    if currentNode.right is None:
                        currentNode.right = newNode
                        break
                    currentNode = currentNode.right
                elif data < currentNode.data:
                    if currentNode.left is None:
                        currentNode.left = newNode
                        break
                    currentNode = currentNode.left
        return self.root

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        self.lst.append(node.data)
        self.inOrder(node.right)


def closestValue(rootNode, value):
    cValue = None
    tree.inOrder(rootNode)
    for i in tree.lst:
        cValue = i
        if i == value or i > value:
            break

    print('Closest value of', value, ':', cValue)



    '''
    cValue = None
    currentNode = rootNode
    while currentNode is not None:
        if value == currentNode.data:
            cValue = value
            break
        if value > currentNode.data:
            if currentNode.right is None:
                cValue = currentNode.data
                break
            currentNode = currentNode.right

        elif value < currentNode.data:
            if currentNode.left is None:
                cValue = currentNode.data
                break
            currentNode = currentNode.left

    print('Closest value of', value, ':', cValue)

    '''



inp, k = input('Enter Input : ').split('/')

k = int(k)
inp = [int(i) for i in inp.split()]

tree = BinarySearchTree()

for i in inp:
    root = tree.insert(i)
    tree.printTree(root)
    print('--------------------------------------------------')

closestValue(root, k)
