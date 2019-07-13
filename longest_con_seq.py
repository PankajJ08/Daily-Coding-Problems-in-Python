"""Given an unsorted array of integers,
find the length of the longest consecutive elements sequence.

For example, given [100, 4, 200, 1, 3, 2],
the longest consecutive element sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.
"""


def lcs(arr):
    """Function to return the longest consecutive sequence in the given array."""
    ans = 0
    s = set()

    for i in arr:
        s.add(i)

    for i in range(len(seq)):
        if arr[i] - 1 not in s:
            j = arr[i]

            while j in s:
                j += 1

            ans = max(ans, j - arr[i])

    return ans


seq = [100, 4, 200, 1, 3, 2]
print("Longest consecutive sequence = ", lcs(seq))
