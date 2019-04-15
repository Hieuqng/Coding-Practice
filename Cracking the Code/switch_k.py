"""
@Problem:
Write a function that rotates a list by k elements. 
For example, [1, 2, 3, 4, 5, 6] rotated by two becomes [3, 4, 5, 6, 1, 2]. 
Try solving this without creating a copy of the list. 
How many swap or move operations do you need?
"""
    
def switch_k(A, k):
    reverse(A, 0, k-1)
    reverse(A, k, len(A)-1)
    reverse(A, 0, len(A)-1)
    return A


def reverse(A, i, j):
    while i < j:
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1
    # return A


if __name__ == "__main__":
    A = [1,2,3,4,5,6]

    print(switch_k(A, 3)) 