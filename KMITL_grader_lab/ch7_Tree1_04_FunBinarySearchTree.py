class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.item = []

    def size(self):
        return len(self.item)

    def isEmpty(self):
        return self.size() == 0

    def enQ(self, data):
        self.item.append(data)

    def deQ(self):
        return self.item.pop(0)

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

    def preOrder(self, node):
        if node is None:
            return
        print(node, '', end='')
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node is None:
            return
        self.inOrder(node.left)
        print(node, '', end='')
        self.inOrder(node.right)

    def postOrder(self, node):
        if node is None:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node, '', end='')

    def breadthFirstSearch(self):
        storeNode = Queue()
        storeNode.enQ(self.root)
        while not storeNode.isEmpty():
            popNode = storeNode.deQ()
            print(popNode, '', end='')
            if popNode.left is not None:
                storeNode.enQ(popNode.left)
            if popNode.right is not None:
                storeNode.enQ(popNode.right)


inp = [int(i) for i in input('Enter Input : ').split()]

tree = BinarySearchTree()

for i in inp:
    root = tree.insert(i)

print('Preorder : ', end='')
tree.preOrder(root)
print('\nInorder : ', end='')
tree.inOrder(root)
print('\nPostorder : ', end='')
tree.postOrder(root)
print('\nBreadth : ', end='')
tree.breadthFirstSearch()
