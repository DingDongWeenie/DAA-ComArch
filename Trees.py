class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.data)


class Trees:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = TreeNode(data)
        else:
            self._insert(self.root, data)

    def _insert(self, node, data):
        if data < node.data:
            if node.left:
                self._insert(node.left, data)
            else:
                node.left = TreeNode(data)
        else:
            if node.right:
                self._insert(node.right, data)
            else:
                node.right = TreeNode(data)

    def in_order(self):
        return self._in_order(self.root)

    def _in_order(self, node):
        return self._in_order(node.left) + [node.data] + self._in_order(node.right) if node else []

    def __str__(self):
        return " -> ".join(map(str, self.in_order()))


if __name__ == "__main__":
    bst = Trees()
    bst.insert(50)
    bst.insert(30)
    bst.insert(70)
    bst.insert(20)
    bst.insert(40)
    bst.insert(60)
    bst.insert(80)
    print("In-order Traversal:", bst)
