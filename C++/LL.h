#include <stdlib.h>

using namespace std;

template <typename T>

struct ListNode {
    T data;
    shared_ptr<ListNode<T> > next;

    ListNode() {
        data = 0;
        next = nullptr;
    }
};


shared_ptr<ListNode<int> > SearchList(shared_ptr<ListNode<int> > L, int key) {
    while (L && L->data != key) {
        L = L->next;
    }

    return L;
}

void InsertAfter(const shared_ptr<ListNode<int> > &node, 
                 const shared_ptr<ListNode<int> > &new_node) {
    new_node->next = node->next;
    node->next = new_node;
}

void DeleteAfter(const shared_ptr<ListNode<int> > &node) {
    node->next = node->next->next;
}

