class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def serialize(root):
    def preorder(node):
        if node:
            values.append(str(node.val))
            preorder(node.left)
            preorder(node.right)
        else:
            values.append("#")

    values = []
    preorder(root)
    return ",".join(values)

def deserialize(data):
    def build_tree(values):
        if not values:
            return None
        val = values.pop(0)
        if val == "#":
            return None
        node = TreeNode(int(val))
        node.left = build_tree(values)
        node.right = build_tree(values)
        return node

    values = data.split(",")
    return build_tree(values)

# Приклад
tree_to_serialize = TreeNode(1, TreeNode(2, TreeNode(3)), TreeNode(4, TreeNode(5)))
serialized_tree = serialize(tree_to_serialize)
# serialized_tree містить "1,2,3,#,#,#,4,5,#,#,#"
deserialized_tree = deserialize(serialized_tree)
# deserialized_tree буде об'єктом, аналогічним tree_to_serialize
