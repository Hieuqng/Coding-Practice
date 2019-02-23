#include <iostream>
#include "LL.h"




int main() {
    // Same as: auto dummy_head = make_shared<ListNode<int> >();
    // This will make dummy_head point to a ListNode, by default generated with 0 and nullptr
    shared_ptr<ListNode<int> > dummy_head(new ListNode<int>);
    shared_ptr<ListNode<int> > n1(new ListNode<int>), n2(new ListNode<int>);
    dummy_head->next = n1;
    n1->next = n2;
    n1->data = 1;
    n2->data = 2;

    shared_ptr<ListNode<int> > curr(dummy_head);
    while (curr != nullptr) {
        cout << curr->data << endl;
        curr = curr->next;
    }

    return 0;
}