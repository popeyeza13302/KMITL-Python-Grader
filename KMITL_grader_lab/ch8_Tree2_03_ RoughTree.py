class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)

class Queue:
    def __init__(self):
        self.lst = []

    def __str__(self):
        s = ''
        for i in self.lst:
            s += str(i.data)
        return '[ ' + str(s) +' ]'

    def size(self):
        return len(self.lst)

    def isEmpty(self):
        return self.size() == 0

    def enQ(self, data):
        self.lst.append(data)

    def deQ(self):
        return self.lst.pop(0)

class BinarySearchTree:
    def __init__(self):
        self.root = Node(0)

    def insert(self, inputList, nodeAmount):    # breadth first search
        queue = Queue()
        queue.enQ(self.root)
        index = 0
        count = 1   #
        for i in range(nodeAmount):
            currentNode = queue.deQ()

            if currentNode.left is None:

                if count >= len(inputList) - 1:
                    currentNode.left = Node(inputList[index])   # insert number in List
                    index += 1  # insert ... index increasing
                else:
                    currentNode.left = Node(0)                  # insert Zero (always newNode)

                count += 1  # count every single enQ
                queue.enQ(currentNode.left)

            if currentNode.right is None:

                if count >= len(inputList) - 1:
                    currentNode.right = Node(inputList[index])  # insert number in List
                    index += 1  # insert ... index increasing
                else:
                    currentNode.right = Node(0)                 # insert Zero (always newNode)

                count += 1  # count every single enQ
                queue.enQ(currentNode.right)

            if count == nodeAmount:     # complete amount of Node
                break

        return self.root

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level+1)
        print('     '*level, node)
        self.printTree(node.left, level+1)

    def recurNode(self, node):      # depth first search

        if node.left is None and node.right is None:    # check if it is last node
            return node.data                        # return last node data

        left = self.recurNode(node.left)
        right = self.recurNode(node.right)

        if left > right:        # find lessValue
            lessValue = right
        else:
            lessValue = left
        node.data = lessValue   # assign new parent Node

        node.right.data = node.right.data - lessValue   # assign son left
        node.left.data = node.left.data - lessValue     # assign son right

        return lessValue

    def calcurateNumber(self):       # breadth first search
        queue = Queue()
        queue.enQ(self.root)
        count = 0

        while not queue.isEmpty():
            currentNode = queue.deQ()
            count += currentNode.data   # plus data of every node in tree
            if currentNode.left is not None:
                queue.enQ(currentNode.left)
            if currentNode.right is not None:
                queue.enQ(currentNode.right)

        print(count)






k, inp = input('Enter Input : ').split('/')

k = int(k)
inp = [int(i) for i in inp.split()]

tree = BinarySearchTree()

if len(inp) == k//2+1:
    root = tree.insert(inp, k)          # insert with breadth first search
    #tree.printTree(node)
    tree.recurNode(root)                # recursion of lessValue
    #print('------------------')
    #tree.printTree(node)
    tree.calcurateNumber()                   # plus every Value in tree
else:
    print('Incorrect Input')
