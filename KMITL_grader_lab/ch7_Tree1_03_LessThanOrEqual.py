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
        self.count = 0

    def insert(self, data):
        newNode = Node(data)
        if self.root is None:
            self.root = newNode
        else:
            currentNode = self.root
            while True:
                if data > currentNode.data:
                    if currentNode.right is not None:
                        currentNode = currentNode.right
                    else:
                        currentNode.right = newNode
                        break
                elif data < currentNode.data:
                    if currentNode.left is not None:
                        currentNode = currentNode.left
                    else:
                        currentNode.left = newNode
                        break

        return self.root

    def printTree(self, node, level=0):
        if node is None:
            return

        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)

    def inOrder(self, node, num):
        if node is None:
            return self.count

        self.count = self.inOrder(node.left, num)
        self.count = self.inOrder(node.right, num)

        if node.data <= num:
            return self.count + 1
        else:
            return self.count


inp, k = [str(i) for i in input('Enter Input : ').split('/')]
inp = inp.split()
k = int(k)

tree = BinarySearchTree()

for i in inp:
    root = tree.insert(int(i))

tree.printTree(root)
print('--------------------------------------------------')
print(tree.inOrder(root, k))
