class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build_tree_from_preorder(preorder):
    def helper(lower=float('-inf'), upper=float('inf')):
        nonlocal idx
        if idx == len(preorder):
            return None

        val = preorder[idx]
        if val < lower or val > upper:
            return None

        idx += 1
        root = TreeNode(val)
        root.left = helper(lower, val)
        root.right = helper(val, upper)
        return root

    idx = 0
    return helper()

# Приклади
preorder_example_1 = "1-2--3--4-5--6--7"
tree_1 = build_tree_from_preorder(preorder_example_1)
# tree_1 буде об'єктом, аналогічним [1,2,5,3,4,6,7]

preorder_example_2 = "1-2--3---4-5--6---7"
tree_2 = build_tree_from_preorder(preorder_example_2)
# tree_2 буде об'єктом, аналогічним [1,2,5,3,null,6,null,4,null,7]

preorder_example_3 = "1-401--349---90--88"
tree_3 = build_tree_from_preorder(preorder_example_3)
# tree_3 буде об'єктом, аналогічним [1,401,null,349,88,90]
