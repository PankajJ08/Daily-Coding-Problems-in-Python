"""Given an array of positive integers, divide the array into two subsets such that
the difference between the sum of the subsets is as small as possible.
And return the difference.

For example, given [5, 10, 15, 20, 25], return the sets {10, 25} and {5, 15, 20},
which has a difference of 5, which is the smallest possible difference"""
import sys


def find_min_recursive(arr, i, total_sum, first_sum):
    """Recursive Solution"""
    if not i:
        return abs(total_sum - 2*first_sum)

    return min(find_min_recursive(arr, i - 1, total_sum, first_sum + arr[i - 1]),
               find_min_recursive(arr, i - 1, total_sum, first_sum))


def find_min(arr):
    n = len(arr)
    first_sum = 0

    total_sum = sum(arr)

    return find_min_recursive(arr, n, total_sum, first_sum)


def dp_solution(arr):
    """Solution using dynamic programming"""
    n = len(arr)
    sum_total = sum(arr)

    dp = [[False for _ in range(sum_total//2 + 1)]
          for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = True

    for i in range(1, n + 1):
        for j in range(1, sum_total//2 + 1):
            dp[i][j] = dp[i - 1][j]
            if arr[i - 1] <= j:
                dp[i][j] |= dp[i - 1][j - arr[i - 1]]

    ans = sys.maxsize
    for j in range(sum_total // 2, -1, -1):
        if dp[n][j]:
            ans = sum_total - 2*j
            break

    return ans


a = [3, 7, 12, 15, 25, 45]
# print(find_min(a))
print(dp_solution(a))
