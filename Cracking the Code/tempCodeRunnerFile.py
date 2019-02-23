
    TEST merge_k
    LL = merge_k([LL1.head, LL2.head])
    while LL:
        print(LL.data, end=' ')
        LL = LL.next