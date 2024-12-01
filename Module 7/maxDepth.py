class Node:
    def __init__(self,d):
        self.data = d
        self.left = None
        self.right = None

def heightTree(node):
    if node == None:
        return 0 # Nodes from node to leaf
    else:
        left = heightTree(node.left)
        right = heightTree(node.right)
        return 1 + max(left,right)

def heightTree2(node):
    if node == None:
        return -1 # Edges node to leaf
    else:
        left = heightTree(node.left)
        right = heightTree(node.right)
        if left > right:
            return 1 + left
        else:
            return 1 + right
