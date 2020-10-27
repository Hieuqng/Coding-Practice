'''
Given n non-negative integers representing an elevation map where the width of each bar is 1,
compute how much water it is able to trap after raining.
'''


def trap(height):
    ans = 0
    size = len(height)

    for i in range(size):
        max_left = 0
        max_right = 0
        for j in range(i, -1, -1):
            max_left = max(max_left, height[j])

        for j in range(i, size):
            max_right = max(max_right, height[j])

        ans += min(max_left, max_right) - height[i]

    return ans


if __name__ == "__main__":
    print(trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
