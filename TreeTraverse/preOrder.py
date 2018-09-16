class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None 

def preOrderRecur(root):
    if not root:
        return
    
    print root.val
    preOrderRecur(root.left)
    preOrderRecur(root.right)

def preOrderIter(root):
    if not root:
        return
    
    stack = []
    node = root
    while node or stack:
        while node:
            print node.val
            stack.append(node)
            node = node.left
        node = stack.pop()
        node = node.right