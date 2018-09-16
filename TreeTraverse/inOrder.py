class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def inOrderRecur(root):
    if not root:
        return
    
    inOrderRecur(root.left)
    print root.val
    inOrderRecur(root.right)


def inOrderIter(root):
    if not root:
        return
    
    stack = []
    node = root
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
        print node.val
        node = node.right