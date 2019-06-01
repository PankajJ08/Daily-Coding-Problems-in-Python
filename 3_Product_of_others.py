""" Given an array of integers,
return a new array such that each element at index i of the new array
is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5],
the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

# ---with division---
def product_others(a, arr_size):
    p = 1
    for i in range(0, arr_size):
        p = p * a[i]
    product = [p // a[i] for i in range(0, arr_size)]
    return product


# ---without division---
def product_opt(arr, arr_size):
    left = [0] * arr_size
    right = [0] * arr_size
    left[0] = 1
    right[-1] = 1
    for i in range(1, arr_size):
        left[i] = (arr[i - 1] * left[i - 1])
    for i in range(arr_size - 2, -1, -1):
        right[i] = (arr[i + 1] * right[i + 1])
    product = [left[i] * right[i] for i in range(0, arr_size)]
    return product


inp = [2, 6, 3, 9, 5]
print("Output: ", product_opt(inp, len(inp)))
