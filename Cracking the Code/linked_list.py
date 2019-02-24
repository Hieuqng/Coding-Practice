class Node():
    def __init__(self, value=0):
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


# def merge_k(lists):
#     # lists contains the heads of every individual lists. 
#     dummy_head = Node()
#     tail = dummy_head
    
#     while len(lists) > 1: #O(k*n) with k = len(lists)
#         value = [l.data for l in lists]

#         # Find minimum among the heads: O(n)
#         minimum = value[0]
#         ind = 0
#         for i, v in enumerate(value):
#             if v <= minimum: 
#                 minimum = v
#                 ind = i

#         tail.next = lists[ind] # Attach the next min value to the tail
#         tail = tail.next # Update the tail

#         # If one list comes to an end, that means we use up all of its elements
#         # remove it from the lists: O(n)
#         if lists[ind].next == None:
#             lists.remove(lists[ind])
#         else:
#             lists[ind] = lists[ind].next
    
#     tail.next = lists[0]

#     return dummy_head.next


def merge_k(lists):
    # Same as above but syntactically shorter
    new_head = tail = Node()
    while any(lst is not None for lst in lists):
        # Get min of all non-None lists
        current_min, i = min((lst.data, i) for i, lst in enumerate(lists) if lst is not None)
        lists[i] = lists[i].next
        tail.next = Node(current_min)
        tail = tail.next
    return new_head.next


def merge_k_with_heap(lists):
    import heapq

    new_head = current = Node()
    heap = [(lst.data, i) for i, lst in enumerate(lists)]
    heapq.heapify(heap)
    while heap:
        current_min, i = heapq.heappop(heap)
        # Add next min to merged linked list.
        current.next = Node(current_min)
        current = current.next
        # Add next value to heap.
        if lists[i] is not None:
            heapq.heappush(heap, (lists[i].data, i))
            lists[i] = lists[i].next
    return new_head.next


def reverse_list(head, start, end):
    dummy_head = Node(0)
    dummy_head.next = head
    sublist_head = dummy_head

    # We want to stop right before the start (at x below)
    # dummy_head -> head -> x -> start -> y -> end -> z -> null
    #       (0) ->  (1) -> (2) -> (3) -> (4) -> (5) -> (6) -> null
    for _ in range(start-1):
        sublist_head = sublist_head.next
    
    # At each loop, we initially have: head->iter->temp->X
    # We want to move temp such that: head->temp->iter->X
    # Next loop would be: head->temp1->temp2->iter->X
    # Number of loops = Number of temp swap = end - start
    sublist_iter = sublist_head.next
    for _ in range(end-start):
        # start from right to left (inside the list out)
        temp = sublist_iter.next
        sublist_iter.next = temp.next
        temp.next = sublist_head.next
        sublist_head.next = temp

    return dummy_head.next


def is_cyclic(head):
    # We will use runner approach: the slow goes one by one, the fast goes two at once.
    # Why 2? Probably 2 is the minimum size to have a cycle

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            # Find cycle length
            slow = slow.next
            cycle_len = 1
            while slow != fast:
                cycle_len += 1
                slow = slow.next
            
            # Find cycle start
            iter_head = head
            runner = head
            
            # Fast forward runner by cycle_len
            for _ in range(cycle_len):
                runner = runner.next
            
            # iter and runner go at same pace
            # after (size - cycle_len): runner loops to the start of the cycle, meets iter.
            while iter_head != runner:
                iter_head = iter_head.next
                runner = runner.next
            return(iter_head, cycle_len)

    return(None, None)
    


if __name__ == '__main__':
    LL1 = LinkedList()
    LL2 = LinkedList()

    for i in [-10, 0, 2, 5, 7]:
        LL1.append(Node(i))

    for i in [-5, -1, 3, 5, 10]:
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

    # TEST reverse_list
    # LL1_reversed = reverse_list(LL1.head, 1, 2)
    # while LL1_reversed:
    #     print(LL1_reversed.data)
    #     LL1_reversed = LL1_reversed.next

    # TEST merge_k
    # LL = merge_k([LL1.head, LL2.head])
    # while LL:
    #     print(LL.data, end=' ')
    #     LL = LL.next
    
    # TEST cyclic
    tail = Node(10)
    LL1.append(tail)
    tail.next = LL1.head.next.next
    cycle_start, cycle_len = is_cyclic(LL1.head)
    print(cycle_start.data, cycle_len)
    

    
