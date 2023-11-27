class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def min_camera_cover(root):
    def dfs(node):
        nonlocal result
        if not node:
            return 2  # Null node is covered

        left = dfs(node.left)
        right = dfs(node.right)

        if left == 0 or right == 0:
            result += 1  # If the left or right child needs a camera, install it on the current node
            return 1  # Current node has a camera

        if left == 1 or right == 1:
            return 2  # If the left or right child has a camera, the current node is covered

        return 0  # If the left and right children are covered, the current node is not covered

    result = 0
    if dfs(root) == 0:
        result += 1  # If the root is not covered, install a camera at the root
    return result

# Приклади
tree_camera_example_1 = TreeNode(0, TreeNode(0, TreeNode(0)))
print(min_camera_cover(tree_camera_example_1))  # Виведе 1

tree_camera_example_2 = TreeNode(0, TreeNode(0, None, TreeNode(0)), TreeNode(0))
print(min_camera_cover(tree_camera_example_2))  # Виведе 1
