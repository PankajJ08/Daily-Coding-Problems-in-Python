"""Given a list of numbers, create an algorithm that arranges them
in order to form the largest possible integer.
For example, given [10, 7, 76, 415], you should return 77641510."""
from functools import cmp_to_key as cmp_k


def compare_it(a, b):
    new_a = int(str(a) + str(b))
    new_b = int(str(b) + str(a))

    return new_a - new_b


def largest_no(arr):
    x = [str(i) for i in sorted(arr, key=cmp_k(compare_it), reverse=True)]
    return "".join(x)


def alternate_way(arr):
    n = len(str(max(arr)))
    extend_arr = [(str(i)*n, i) for i in arr]
    extend_arr.sort(reverse=True)
    return "".join([str(i[1]) for i in extend_arr])


inp = [777, 0, 761, 4152]
print(largest_no(inp))
print(alternate_way(inp))
