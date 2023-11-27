from collections import defaultdict, deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def vertical_order_traversal(root):
    if not root:
        return []

    column_table = defaultdict(list)
    queue = deque([(root, 0)])

    while queue:
        node, column = queue.popleft()
        column_table[column].append(node.val)

        if node.left:
            queue.append((node.left, column - 1))
        if node.right:
            queue.append((node.right, column + 1))

    return [column_table[col] for col in sorted(column_table)]

# Приклади
tree_vertical_example_1 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(vertical_order_traversal(tree_vertical_example_1))
# Виведе [[9], [3, 15], [20], [7]]

tree_vertical_example_2 = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4), TreeNode(5))), TreeNode(6, TreeNode(7)))
print(vertical_order_traversal(tree_vertical_example_2))
# Виведе [[4], [3], [2], [1, 5, 6], [7]]
