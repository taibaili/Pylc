class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    # Insert a single element
    # def insert(self, x):
    #     if (self.root == None):
    #         self.root = TreeNode(x)
    #     else:
    #         self._insert(self, x, self.root)
    #
    # def _insert(self, node, x):
    #     if (x < node.val):
    #         if (node.left == None):
    #             node.left = TreeNode(x, node)
    #         else:
    #             self._insert(x, node.left)
    #     else:
    #         if (node.right == None):
    #             node.right = TreeNode(x, node)
    #         else:
    #             self._insert(x, node.right)

def insert(root, value):
    if not root:
        return TreeNode(value)
    elif value < root.val:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def create_tree_from_list(seq):
    root = None
    for word in seq:
        root = insert(root, word)
    return root

def search(root, word, depth=1):
    if not root:
        return 0, 0
    elif root.value == word:
        return depth, root.count
    elif word < root.value:
        return search(root.left, word, depth + 1)
    else:
        return search(root.right, word, depth + 1)

def print_tree(root):
    if root:
        print_tree(root.left)
        print
        root
        print_tree(root.right)

if __name__ == '__main__':
    src = ['a', 'b', 'c', 'd', 'e']
    tree = create_tree_from_list(src)
    print_tree(tree)

    # Output
    # value: bar, count: 2
    # value: barfoo, count: 1
    # value: foo, count: 1
    # value: foobar, count: 1