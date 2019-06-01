""" Given a list of numbers, return whether any two sums to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""


def has_sum(a, a_size, p_sum):
    b = set()
    for i in range(0, a_size):
        temp = p_sum - a[i]
        if temp in b:
            print("Pair with the given sum: {} and {}".format(temp, a[i]))
            b.remove(temp)
        b.add(a[i])


arr = [2, 3, 3, 4]
m = 5
has_sum(arr, len(arr), m)
