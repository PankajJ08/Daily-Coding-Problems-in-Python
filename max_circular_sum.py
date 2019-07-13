"""Given a circular array, compute its maximum subarray sum in O(n) time.

For example, given [8, -1, 3, 4], return 15 as we choose the numbers 3, 4,
and 8 where the 8 is obtained from wrapping around."""


def kadane_sum(arr):
    n = len(arr)
    max_sum = arr[0]
    max_curr = arr[0]

    for i in range(1, n):
        max_curr = max(arr[i] + max_curr, arr[i])
        max_sum = max(max_sum, max_curr)

    return max_sum


def circular_sum(arr):
    max_kadane = kadane_sum(arr)
    max_wrap = 0

    for i in range(len(arr)):
        max_wrap += arr[i]
        arr[i] = -arr[i]

    max_wrap += kadane_sum(arr)

    if max_kadane > max_wrap or not max_wrap:
        return max_kadane
    else:
        return max_wrap


a = [-8, 2, -1, -5]
print(circular_sum(a))
