class BST:

    def deletion(self, node, data):

        if node is None:
            return

        if node.data != data:
            if data > node.data:
                node.right = self.deletion(node.right,data)
            elif data < node.data:
                node.left = self.deletion(node.left,data)

        elif node.data == data:   # found!

            if node.left is None:
                node = node.right
                return node
            elif node.right is None:
                node = node.left
                return node
            else:
                current = node.left
                while current.right is not None:
                    current = current.right

                node.data = current.data
                node.left = self.deletion(node.left, current.data)

        return node

