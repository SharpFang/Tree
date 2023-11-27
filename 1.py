class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False
    return is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)

# Приклади
p1 = TreeNode(1, TreeNode(2), TreeNode(3))
q1 = TreeNode(1, TreeNode(2), TreeNode(3))
print(is_same_tree(p1, q1))  # Виведе True

p2 = TreeNode(1, TreeNode(2))
q2 = TreeNode(1, None, TreeNode(2))
print(is_same_tree(p2, q2))  # Виведе False

p3 = TreeNode(1, TreeNode(2, TreeNode(1)), TreeNode(3))
q3 = TreeNode(1, TreeNode(1, TreeNode(2)), TreeNode(3))
print(is_same_tree(p3, q3))  # Виведе False
