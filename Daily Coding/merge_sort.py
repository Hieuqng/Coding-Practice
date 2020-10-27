def merge(arr, low, mid, high):
    n_left = mid-low+1
    n_right = high-mid

    left = [0] * (n_left)
    right = [0] * (n_right)

    for i in range(n_left):
        left[i] = arr[low+i]

    for j in range(n_right):
        right[j] = arr[mid+1+j]
    
    i = j = 0
    k = low

    while i < n_left and j < n_right:
        left_val = left[i]
        right_val = right[j]

        if left_val <= right_val:
            arr[k] = left_val
            i += 1
        
        elif right_val < left_val:
            arr[k] = right_val
            j += 1

        k += 1

    while i < n_left:
        arr[k] = left[i]
        i = i + 1
        k = k + 1

    while j < n_right:
        arr[k] = right[j]
        j = j + 1
        k = k + 1


def mergesort(arr, low, high):
    if low < high:
        mid = int((low+high) / 2)
        mergesort(arr, low, mid)
        mergesort(arr, mid+1, high)
        merge(arr, low, mid, high)

if __name__ == '__main__':
    arr = [1,5,7,9,2,3,6,10, 0]
    mergesort(arr, 0, len(arr)-1)
    print(arr)
