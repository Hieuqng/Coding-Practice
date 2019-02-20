class Node():
    def __init__(self, value=None):
        self.data = value
        self.next = None


class LinkedList():
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head == None:
            self.head = node
            return

        curr = self.head
        while curr.next != None:
            curr = curr.next

        curr.next = node
        return

    def search(self, value):
        curr = self.head
        while curr and curr.data != value:
            curr = curr.next

        return curr

    def print(self):
        curr = self.head
        while curr != None:
            print(curr.data, end=' ')
            curr = curr.next
        return


def merge(list1, list2):
    curr1 = list1.head
    curr2 = list2.head

    dummy_head = Node()
    tail = dummy_head

    while curr1 and curr2:
        if curr1.data > curr2.data:
            tail.next = curr2
            tail = tail.next
            curr2 = curr2.next
        else:
            tail.next = curr1
            tail = tail.next
            curr1 = curr1.next

    if curr1:
        tail.next = curr1
    else:
        tail.next = curr2

    return dummy_head.next


if __name__ == '__main__':
    LL1 = LinkedList()
    LL2 = LinkedList()

    for i in [2, 5, 7]:
        LL1.append(Node(i))

    for i in [3, 5, 11]:
        LL2.append(Node(i))

    # TEST search
    # res = LL.search(3)
    # if res:
    #     print(res.data)

    # TEST merge
    # LL = merge(LL1, LL2)
    # while LL:
    #     print(LL.data)
    #     LL = LL.next
