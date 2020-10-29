class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # GeeksForGeeks use leaf height = 1

    def __str__(self):
        return str(self.data)


class AVLTree:
    def get_height(self, root):
        if root is None:
            return 0        # nothing... return 0 height ( default None = 0 ...not -1)
        return root.height  # else return root height (normally 1)

    def get_balance(self, root):
        if root is None:    # root is parent Node
            return 0        # noting...
        return self.get_height(root.left) - self.get_height(root.right)     # H.left - H.right

    def right_rotate(self, x):
        # init                  # z <- [y] <- x(node)
        y = x.left
        tempTree = y.right     # store tempTree

        # rotate
        y.right = x          # [y] -> x(node)
        x.left = tempTree    # tempTree <-x(node)

        # update new height
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # new root after rotation
        return y

    def left_rotate(self, x):
        # init                  # x(node) -> [y] -> z
        y = x.right
        tempTree = y.left

        # rotate
        y.left = x
        x.right = tempTree

        # update new height
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        # new root after rotation
        return y

    def insert(self, node, data):
        # normal insertion
        if node is None:        # base case 1st
            return Node(data)
        elif data < node.data:
            node.left = self.insert(node.left, data)    # left < currentNode
        elif data > node.data:
            node.right = self.insert(node.right, data)         # currentNode < right

        # update height of parent node
        node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))  # itself + max(H.left,H.right)

        # prepare to balance...
        balance = self.get_balance(node)    # different of H.left and H.right

        # balance ok = [ -1, 0 ,1 ]
        # balance not ok (need rotate) = [ x<-1 or x>1 ]
        if balance > 1 and data < node.left.data:       # normal rotate right   (H.left > H.right)      #  new data <- y
            return self.right_rotate(node)

        if balance < -1 and data > node.right.data:     # normal rotate left    (H.right > H.left)      #  y -> new data
            return self.left_rotate(node)

        if balance > 1 and data > node.left.data:       # special case 1st  # y -> new data
            node.left = self.left_rotate(node.left)   # left first(node.left) then right
            return self.right_rotate(node)

        if balance < -1 and data < node.right.data:     # special case 2nd  # new data <- y
            node.right = self.right_rotate(node.right)   # right first(node.right) then left
            return self.left_rotate(node)

        # don't forget to return ^^^

        # return root node normally
        return node

    def preorder(self, root):
        if not root:
            return
        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def printTree(self, node, level=0):
        if node is None:
            return
        self.printTree(node.right, level + 1)
        print('     ' * level, node)
        self.printTree(node.left, level + 1)


if __name__ == '__main__':
    tree = AVLTree()
    root = None

    root = tree.insert(root, 10)
    root = tree.insert(root, 20)
    root = tree.insert(root, 30)
    root = tree.insert(root, 40)
    root = tree.insert(root, 50)
    root = tree.insert(root, 25)

    tree.printTree(root)
    tree.preorder(root)
