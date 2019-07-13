"""Find the sum of contiguous subarray within a one-dimensional array
 of numbers which has the largest sum."""


def max_subarray_v1(arr):
    """Returning maximum subarray-sum using Kadane's algorithm.
    :rtype: int
    """
    n = len(arr)
    max_so_far = arr[0]
    max_ending_here = arr[0]

    for i in range(1, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


def max_subarray_v2(arr):
    """Function that return only non-negative sum.
    return 0 if all elements are negative. """
    n = len(arr)
    max_so_far = 0
    max_ending_here = 0

    for i in range(0, n):
        max_ending_here = max(arr[i], max_ending_here + arr[i])
        if max_ending_here > 0:
            max_so_far = max(max_so_far, max_ending_here)

    return max_so_far


if __name__ == '__main__':
    array = [5, -1, -8, -9]
    print("Maximum subarray-sum = ", max_subarray_v2(array))
