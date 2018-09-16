class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def levelOrder(root):
    if not root:
        return

    queue = []
    node = root
    queue.append(node)
    while queue:
        node = queue.pop(0)
        print node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

