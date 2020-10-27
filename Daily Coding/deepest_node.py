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


#--------------------------------------------------------------#


##########
## SELF ##
##########
def is_binary(head):
    if head == None:
        return True
    
    if head.left and head.left.data > head.data:
        return False
    if head.right and head.right.data < head.data:
        return False
    if not is_binary(head.left) or not is_binary(head.right):
        return False
    
    return True


##########
## WEB  ##
##########
def is_bst(root):
    def is_bst_helper(root, min_key, max_key):
        if root is None:
            return True
        if root.key <= min_key or root.key >= max_key:
            return False
        return is_bst_helper(root.left, min_key, root.key) and \
               is_bst_helper(root.right, root.key, max_key)

    return is_bst_helper(root, float('-inf'), float('inf'))


#--------------------------------------------------------------#


###########
## DEBUG ##
###########
def height(root):
    if not root:
        return 0

    left =  height(root.left)
    right = height(root.right)

    if left < right:
        return right + 1
    else:
        return left + 1


# def print_tree(root):
#     if root == None:
#         print('.', end=' ')
#         return

#     print(root.data, end=' ')
#     print_tree(root.left)
#     print_tree(root.right)
#     return



if __name__ == "__main__":
    # TEST deepest_node
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

    # TEST is_binary
    #      a
    #    /  \
    #   b    c
    #  / \  / \
    # d  e f   g
    root = Node('5')
    b = Node('2')
    c = Node('6')
    d = Node('1')
    e = Node('3')
    f = Node('5')
    g = Node('7')
    root.left = b
    root.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    print(is_binary(root))



