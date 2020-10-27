import time


def two_sum_hashtable(S, target):
    table = {}
    for i in range(len(S)):
        complement = target - S[i]
        if complement in table:
            return (table[complement], i)
        else:
            table[S[i]] = i
    return False


def two_sum(S, target, skip_first=0):
    '''
    Assume S is sorted (or can be sorted by nlogn like Quicksort)
    '''
    if (S[0] + S[-1]) == target:
        return (skip_first, len(S) - 1 + skip_first)

    else:
        if (S[0] + S[-1]) > target:
            return two_sum(S[:-1], target, skip_first)
        else:
            skip_first += 1
            return two_sum(S[1:], target, skip_first)
    return (-1, -1)


if __name__ == '__main__':
    S = [2, 7, 11, 15, 20, 21, 22, 30]
    target = 33

    print(f"Array: {S} \n Target: {target}")
    start = time.time()
    sum_sorted = two_sum(S, target)
    end = time.time()
    print("If sorted: {} ... took {:.3f} ms".format(sum_sorted, (end - start) * 1000))

    start = time.time()
    sum_hash = two_sum_hashtable(S, target)
    end = time.time()
    print("If sorted: {} ... took {:.3f} ms".format(sum_hash, (end - start) * 1000))
