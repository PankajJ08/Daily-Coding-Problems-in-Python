"""Given a number in the form of a list of digits, return all possible permutations.

For example, given [1,2,3], return [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]"""


def permutations(arr, L, r, out):
    """Function that returns all the permutation for a given list."""
    if L == r:
        out.append(arr[:])

    for i in range(L, r + 1):
        arr[i], arr[L] = arr[L], arr[i]
        permutations(arr, L + 1, r, out)
        arr[i], arr[L] = arr[L], arr[i]         # Backtrack

    return out


a = [1, 2, 3]
print(permutations(a, 0, len(a) - 1, []))
