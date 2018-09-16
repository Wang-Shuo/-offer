class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def postOrderRecur(root):
    if not root:
        return
    
    postOrderRecur(root.left)
    postOrderRecur(root.right)
    print(root.val)


def postOrderIter(root):
    if not root:
        return 
    
    stack1 = []
    stack2 = []
    node = root
    stack1.append(node)
    while stack1:
        node = stack1.pop()
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
        stack2.append(node)
    while stack2:
        print(stack2.pop().val)