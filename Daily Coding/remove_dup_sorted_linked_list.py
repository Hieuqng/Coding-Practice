# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = last = ListNode(0)
        dummy.next = head
        
        while head and head.next: 
            if (head.val != head.next.val):
                last = head         
            else:
                while head.next and (head.val == head.next.val):
                    head = head.next
                last.next = head.next
            head = head.next
            
        return dummy.next

if __name__ == '__main__':
    solver = Solution()
    nodes = [1,1,1,2,3,4,4,5,5,6,7,8,9,10,10,11,12,12,12]
    head = ListNode(nodes[0])
    dummy = ListNode(0, head)
    for i in nodes[1:]:
        node = ListNode(i)
        head.next = node
        head = head.next
    newHead = solver.deleteDuplicates(dummy.next)
    while newHead:
        if newHead.next:
            print(newHead.val, '->', sep='', end='')
        else:
            print(newHead.val)
        newHead = newHead.next

        
        