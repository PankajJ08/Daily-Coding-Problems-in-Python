"""We can determine how "out of order" an array A is by counting the number of inversions it has.
Two elements A[i] and A[j] form an inversion if A[i] > A[j] but i < j.
That is, a smaller element appears after a larger element.

Given an array, count the number of inversions it has. Do this faster than O(N^2) time.

You may assume each element in the array is distinct.

For example, a sorted list has zero inversions.
The array [2, 4, 1, 3, 5] has three inversions: (2, 1), (4, 1), and (4, 3).
The array [5, 4, 3, 2, 1] has ten inversions: every distinct pair forms an inversion."""


def count_inversion_v1(arr):
    """Naive solution to find number of inversions in array."""
    count = 0

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                count += 1

    return count


def count_inversion_v2(arr):
    """Function to count array inversion using modified merge sort."""
    out = arr[:]
    print(merge_sort(arr, out, 0, len(seq) - 1))


def merge_sort(arr, out, low, high):
    """Function to sort a given sequence."""

    if high == low:
        return 0

    mid = (low + high) >> 1
    i_count = 0

    i_count += merge_sort(arr, out, low, mid)
    i_count += merge_sort(arr, out, mid + 1, high)
    i_count += merge(arr, out, low, high, mid)

    return i_count


def merge(arr, out, low, high, mid):
    """Modified merge function to count all the inversions."""
    i_count = 0
    i, j, k = low, mid + 1, low

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            out[k] = arr[i]
            i += 1
            k += 1

        else:
            out[k] = arr[j]
            j += 1
            k += 1

            i_count += mid - i + 1

    while i <= mid:
        out[k] = arr[i]
        i += 1
        k += 1

    for i in range(len(arr)):
        arr[i] = out[i]

    return i_count


seq = [4, 16, 2, 12, 5, 1]
count_inversion_v2(seq)
