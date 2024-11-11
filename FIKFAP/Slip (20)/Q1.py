class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_value):
        self.root = TreeNode(root_value)

    def add(self, value):
        self._add_recursive(self.root, value)

    def _add_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._add_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._add_recursive(node.right, value)

    def dfs(self):
        print("Depth First Search (Pre-order Traversal):")
        self._dfs_util(self.root)

    def _dfs_util(self, node):
        if node is not None:
            print(node.value, end=' ')  
            self._dfs_util(node.left)   
            self._dfs_util(node.right)  

if __name__ == "__main__":
    bt = BinaryTree(5)
    bt.add(3)
    bt.add(7)
    bt.add(2)
    bt.add(4)
    bt.add(6)
    bt.add(8)

    bt.dfs()