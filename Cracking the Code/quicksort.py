def quicksort(arr):
    return quicksort_aux(arr, 0, len(arr)-1)


def quicksort_aux(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quicksort_aux(arr, low, pivot-1)
        quicksort_aux(arr, pivot+1, high)
    return arr


def partition(arr, low, high):
    pivot = arr[low]
    left = low+1
    right = high

    done = False
    while not done:
        while left <= right and arr[left] <= pivot:
            left += 1
        while right >= left and arr[right] >= pivot:
            right -= 1
        
        if right < left:
            done = True
        else:
            arr[right], arr[left] = arr[left], arr[right]
    arr[low], arr[right] = arr[right], arr[low]
    return right


if __name__ == "__main__":
    arr = [54,26,93,17,77,31,44,55,20]
    print(quicksort(arr))
