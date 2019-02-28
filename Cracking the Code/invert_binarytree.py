# Invert a binary tree.

# For example, given the following tree:

#     a
#    / \
#   b   c
#  / \  /
# d   e f
# should become:

#   a
#  / \
#  c  b
#  \  / \
#   f e  d

class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def invert(root):
    # if root is leave, return root
    if not root.left and not root.right:
        return root
    else:
        left = right = None
        if root.left:
            left = invert(root.left)
        if root.right:
            right = invert(root.right)
        root.left, root.right = right, left
    return root


def print_tree(root, vals, level):
    if not root:
        return
    else:
        print_tree(root.left, vals, level+1)
        print_tree(root.right, vals, level+1)
        vals.append((root.data, level))
    return


if __name__ == "__main__":
    a = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    e = Node('e')
    f = Node('f')

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    a = invert(a)
    vals = []
    print_tree(a, vals, 1)
    vals = sorted(vals, key=lambda x: x[1])
    max_level = vals[-1][1]
    curr_level = 1
    pos = 1
    print(vals)
        


