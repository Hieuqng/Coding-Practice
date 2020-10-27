# returns leftmost (or rightmost) index at which `target` should be inserted in sorted
# array `nums` via binary search.


def extreme_insertion_index(nums, target, left):
    lo = 0
    hi = len(nums)

    # Keep searching until lo = hi
    while lo < hi:
        mid = (lo + hi) // 2

        # For left search, nums[mid] may equal target. That allows to continue searching over the small side
        # In case there is a series of same numbers. Notice hi always "decreases", lo always "increases"
        if nums[mid] > target or (left and target == nums[mid]):
            hi = mid
        else:
            lo = mid + 1

    return lo


def searchRange(nums, target):
    left_idx = extreme_insertion_index(nums, target, True)

    # if left is at the end or left is "None" (There is no target in the array)
    if left_idx == len(nums) or nums[left_idx] != target:
        return [-1, -1]

    return [left_idx, extreme_insertion_index(nums, target, False) - 1]


if __name__ == '__main__':
    arr = [1, 2, 5, 5, 5, 6, 7, 8, 8, 8, 10]
    ans = [7, 9]
    print(f"Array: {arr} ... Searching for: 8 ...")
    print("Return: ", searchRange(arr, 8))
    print("Should be: ", ans)
