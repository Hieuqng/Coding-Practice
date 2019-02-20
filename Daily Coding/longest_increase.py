'''
Link: https://www.dailycodingproblem.com/solution/75?token=2726739037079dabbc243781618c9675a2e9840b04e9551dace6af9ffa1e843ada8ff6a1

Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15.
'''


def longest_increasing_subsequence(arr):
    '''
    Assume that we already have a function that gives us the length of the longest increasing subsequence. Then we'll try to feed some part of our input array back to it and try to extend the result. Our base cases are: the empty list, returning 0, and an array with one element, returning 1.

    Then,
    For every index i up until the second to last element, calculate longest_increasing_subsequence up to there.
    We can only extend the result with the last element if our last element is greater than arr[i] (since otherwise, it's not increasing).
    Keep track of the largest result.
    '''

    if not arr:
        return 0
    if len(arr) == 1:
        return 1

    max_ending_here = 0
    for i in range(len(arr)):
        ending_at_i = longest_increasing_subsequence(arr[:i])
        if arr[-1] > arr[i - 1] and ending_at_i + 1 > max_ending_here:
            max_ending_here = ending_at_i + 1
    return max_ending_here


def longest_increasing_subsequence(arr):
    '''
    We'll keep an array A of length N, and A[i] will contain the length of the longest increasing subsequence ending at i. We can then use the same recurrence but look it up in the array instead
    '''

    if not arr:
        return 0
    cache = [1] * len(arr)
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] > arr[j]:
                cache[i] = max(cache[i], cache[j] + 1)
    return max(cache)
