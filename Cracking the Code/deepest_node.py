# Given the root of a binary tree, return a deepest node. 
# For example, in the following tree, return d.
#     a
#    / \
#   b   c
#  /
# d

class Node():
    def __init__(self, value=None):
        self.data = value
        self.left = None
        self.right = None

###########
## Self  ##
###########
def deepest_node(root):
    return max(deepest_node_aux(root, 1, []), key=lambda x: x[0])


def deepest_node_aux(root, h, nodes):
    if not root:
        return nodes

    nodes.append((h, root.data))
    _ = deepest_node_aux(root.left, h+1, nodes)
    _ = deepest_node_aux(root.right, h+1, nodes)
    return nodes


###########
##  Web  ##
###########
def deepest_node2(root):
    if root and not root.left and not root.right:
        return (root, 1)

    if not root.left:
        return increment_height(deepest_node2(root.right))
    if not root.right:
        return increment_height(deepest_node2(root.left))

    return increment_height(
        max(deepest_node2(root.left), deepest_node2(root.right), 
            key=lambda x: x[1]))


def increment_height(info):
    node, height = info
    return (node, height+1)


###########
## DEBUG ##
###########
# def height(root):
#     if not root:
#         return 0

#     left =  height(root.left)
#     right = height(root.right)

#     if left < right:
#         return right + 1
#     else:
#         return left + 1


# def print_tree(root):
#     if root == None:
#         print('.', end=' ')
#         return

#     print(root.data, end=' ')
#     print_tree(root.left)
#     print_tree(root.right)
#     return

if __name__ == "__main__":
    root = Node('a')
    b = Node('b')
    c = Node('c')
    d = Node('d')
    root.left = b
    root.right = c
    b.left = d

    # print_tree(root)
    info = deepest_node2(root)
    print(info[0].data, info[1])