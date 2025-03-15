class TreeNode(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
class AVLtree(object):
    def getHeight(self, node):
        if not node:
            return 0
        return node.height
    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)
    def leftRotate(self, z):
        y = z.right
        w = y.left
        y.left = z
        z.right = w
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    def rightRotate(self, z):
        y = z.left
        w = y.right
        y.right = z
        z.left = w
        z.height = 1 + max(self.getHeight(z.left),
                           self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left),
                           self.getHeight(y.right))
        return y
    def insert_node(self, node, data):
        # find the location to insert
        if not node:      # if the node does not exist
            return TreeNode(data)
        elif data < node.data:
            node.left = self.insert_node(node.left, data)
        else:
            node.right = self.insert_node(node.right, data)
        node.height = 1 + max(self.getHeight(node.left),
                              self.getHeight(node.right))
        # update the balance factor
        balanceFactor = self.getBalance(node)
        if balanceFactor > 1:   # unbalanced to the left
            if data < node.left.data:  # simple right rotation
                return self.rightRotate(node)
            else:                      # double left-right rotation
                node.left = self.leftRotate(node.left)
                return self.rightRotate(node)
        if balanceFactor < -1:   # unbalanced to the right
            if data > node.right.data: # simple left rotation
                return self.leftRotate(node)
            else:                      # double right-left rotation
                node.right = self.rightRotate(node.right)
                return self.leftRotate(node)
        return node
    def printTree(self, node, level=0):
        if node is None:
            return
        print("---"*(level+1), node.data, "({})".format(node.height))
        self.printTree(node.left, level+1)
        self.printTree(node.right, level+1)
def main():
    tree = AVLtree()
    root = None
    a = [56,25,72,12,44,64,88,33,38]
    for data in a:
        root = tree.insert_node(root, data)
        print("===========")
        tree.printTree(root)


main()
