"""
@Problem: Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree. 
Assume that each node in the tree also has a pointer to its parent.

---
@Solution:
"""

class Node:
    def __init__(self, value, left=None, right=None):
        self.parent = None
        self.data = value
        self.left = left
        self.right = right
        if left: 
            left.parent = self
        if right: 
            right.parent = self


def lca(root, a, b):
    def depth(node):
        count = 0
        while node:
            count += 1
            node = node.parent
        return count

    depth_a, depth_b = depth(a), depth(b)
    if depth_a < depth_b:
        while depth_a < depth_b:
            b = b.parent
            depth_b -= 1
    elif depth_a > depth_b:
        while depth_a > depth_b:
            a = a.parent
            depth_a -= 1

    while a and b and (a is not b):
        a = a.parent
        b = b.parent

    return a if (a is b) else None

    

if __name__ == "__main__":
    f = Node('f')
    g = Node('g')
    b = Node('b')
    d = Node('d')
    e = Node('e', f, g)
    c = Node('c', d, e)
    root = Node('a', b, c)

    v = f
    w = d

    print(lca(root, v, w).data)


