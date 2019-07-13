"""An sorted array of integers was rotated an unknown number of times.
Given such an array, find the index of the element in the array in faster than linear time.
If the element doesn't exist in the array, return null.

For example, given the array [13, 18, 25, 2, 8, 10] and the element 8,
return 4 (the index of 8 in the array)."""


def binary_search(arr, key, low, high):
    """Function to implementing binary search."""
    if low > high:
        return

    mid = (low + high) // 2

    if arr[mid] == key:
        return mid
    if arr[mid] > key:
        return binary_search(arr, key, low, mid - 1)
    return binary_search(arr, key, mid + 1, high)


def find_pivot(arr, low, high):
    """Function to return pivot element around which array rotated."""
    if low > high:
        return
    if low == high:
        return low

    mid = (low + high) // 2

    if mid < high and arr[mid] > arr[mid + 1]:
        return mid
    if mid > low and arr[mid] < arr[mid - 1]:
        return mid - 1

    if arr[low] >= arr[mid]:
        return find_pivot(arr, low, mid - 1)
    return find_pivot(arr, mid + 1, high)


def search_array(arr, n, key):
    """Return a index of key element using binary search around pivot."""
    pivot = find_pivot(arr, 0, n)

    if not pivot:
        # array is sorted.
        return binary_search(arr, key, 0, n)

    if arr[pivot] == key:
        return pivot

    if arr[0] <= key:
        return binary_search(arr, key, 0, pivot - 1)
    return binary_search(arr, key, pivot + 1, n)


a = [3, 4, 6, 11, 1, 2]
k = 1
print(search_array(a, len(a) - 1, k))
