"""
@Problem: Given a binary tree, return all paths from the root to leaves.

For example, given the tree:

   1
  / \
 2   3
    / \
   4   5
Return [[1, 2], [1, 3, 4], [1, 3, 5]].

"""
# Two-way Binary Tree
class Node:
    def __init__(self, value, left=None, right=None):
        self.parent = None
        self.value = value
        self.left = left
        self.right = right
        if left:
           left.parent = self
        if right:
           right.parent = self

    def path(self):
        path = []
        current = self
        while current:
            path = [current.value] + path
            current = current.parent
        return path


def find_leaves(node):
    leaves = []
    queue = list()
    queue.append(node)
    while len(queue):
        node = queue.pop()
        if not node.left and not node.right:
            leaves += [node.path()]
            continue
        if node.right:
            queue.append(node.right)
        if node.left:
            queue.append(node.left)
    return leaves


# WARNING!!! We should avoid this practice on large or unknown trees 
# because of the possibility of a call stack overflow.
def bad_find_leaves(node):
    if not node.left and not node.right:
        return [node.path()]
    leaves = []
    if node.left:
        leaves += find_leaves(node.left)
    if node.right:
        leaves += find_leaves(node.right)
    return leaves


if __name__ == "__main__":
    root = Node(
        value=1,
        left=Node(2),
        right=Node(3, Node(4), Node(5))
    )

    print(root.left.path())

    print(find_leaves(root))

