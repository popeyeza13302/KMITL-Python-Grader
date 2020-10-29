class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.data)


treedata = []


class BinarySearchTree:
    global treedata

    def __init__(self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.data:
                    # print('less than', val, '<', current.data)
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.data:
                    # print('greater than', val, '>', current.data)
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    # function to delete element in binary tree
    def deletion(self, node, data):
        if node is None:    # base case
            return

        if node.data != data:   # not found
            if node.data > data:
                node.left = self.deletion(node.left, data)  # not found left
            elif node.data < data:
                node.right = self.deletion(node.right, data)  # not found right

        else:   # found !!!!

            if node.left is None:   # left None
                node = node.right
                return node
            elif node.right is None:  # right None
                node = node.left
                return node
            else:
                current = node.left
                while current.right is not None:
                    current = current.right

                node.data = current.data    # replace delete
                node.left = self.deletion(node.left, current.data)  # permanent delete recursive.....

        return node


def printTree90(node, level=0):
    if node is None:
        return
    printTree90(node.right, level + 1)
    print('     ' * level, node)
    printTree90(node.left, level + 1)

# i 3,i 4,i 5,d 3,d 4,d 5

tree = BinarySearchTree()
data = input("Enter Input : ").split(",")
for i in range(len(data)):
    data[i] = data[i].split()
    if data[i][0] == 'd':
        print("delete " + (data[i][1]))
        tree.root = tree.deletion(tree.root, int(data[i][1]))
        printTree90(tree.root)
    elif data[i][0] == 'i':
        print("insert " + (data[i][1]))
        tree.insert(int(data[i][1]))
        printTree90(tree.root)


