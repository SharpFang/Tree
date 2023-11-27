class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def kth_smallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.val
        root = root.right

# Приклади
bst_example = TreeNode(3, TreeNode(1, None, TreeNode(2)), TreeNode(4))
print(kth_smallest(bst_example, 1))  # Виведе 1

bst_example_2 = TreeNode(5, TreeNode(3, TreeNode(2, TreeNode(1)), TreeNode(4)), TreeNode(6))
print(kth_smallest(bst_example_2, 3))  # Виведе 3
