"""Given an array and a permutation, apply the permutation to the array. For example,
given the array ["a", "b", "c"] and the permutation [2, 1, 0], return ["c", "b", "a"]."""


def apply_permutation(arr, p):
    out = []
    for i in p:
        out.append(arr[i])

    return out


arr = ['a', 'b', 'c', 'd', 'e']
p = [0, 4, 3, 2, 1]
print(apply_permutation(arr, p))