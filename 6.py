class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def max_path_sum(root):
    def max_gain(node):
        nonlocal max_sum
        if not node:
            return 0
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)
        path_sum = node.val + left_gain + right_gain
        max_sum = max(max_sum, path_sum)
        return node.val + max(left_gain, right_gain)

    max_sum = float('-inf')
    max_gain(root)
    return max_sum

# Приклади
tree_example_1 = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))
print(max_path_sum(tree_example_1))  # Виведе 15

tree_example_2 = TreeNode(-10, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(max_path_sum(tree_example_2))  # Виведе 42
