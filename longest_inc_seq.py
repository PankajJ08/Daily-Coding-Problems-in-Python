"""Given an array of numbers, find the length of the longest increasing subsequence in the array.
The subsequence does not necessarily have to be contiguous.

For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15],
the longest increasing subsequence has length 6: it is 0, 2, 6, 9, 11, 15."""


def lis_v1(arr, n, max_len=1):
    """Recursive function to find longest increasing subsequence in the given array."""
    max_end = 1

    if n == 1:
        return 1

    for i in range(1, n):
        res = lis_v1(arr, i, max_len)

        if arr[i - 1] < arr[n - 1] and max_end < res + 1:
            max_end = res + 1

    max_len = max(max_len, max_end)

    return max_len


def lis_v2(arr, n):
    """Function based on Dynamic Programming to return longest increasing subsequence."""
    lis = [1] * n

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1

    max_len = 0

    for i in range(n):
        max_len = max(max_len, lis[i])

    return max_len


seq = [0, 1, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 10, 11, 15]
print("Maximum increasing subsequence = ", lis_v2(seq, len(seq)))
