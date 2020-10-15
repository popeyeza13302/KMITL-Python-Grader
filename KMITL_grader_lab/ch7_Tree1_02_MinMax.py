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
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
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

    def min(self):
        currentNode = self.root
        while currentNode.left is not None:
            currentNode = currentNode.left

        return currentNode.data  # left side for Min

    def max(self):
        currentNode = self.root
        while currentNode.right is not None:
            currentNode = currentNode.right

        return currentNode.data  # right side for Max

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)


inp = [int(i) for i in input('Enter Input : ').split()]

tree = BinarySearchTree()

for i in inp:
    root = tree.insert(i)

tree.printTree(root)
minValue, maxValue = tree.min(), tree.max()
print('--------------------------------------------------')
print('Min :', minValue)
print('Max :', maxValue)
