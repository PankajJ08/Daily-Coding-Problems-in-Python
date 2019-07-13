"""Given an integer list where each number represents the number of hops you can make,
determine whether you can reach to the last index starting at index 0.

For example, [2, 0, 1, 0] returns true while [1, 1, 0, 1] returns false."""


def hop_to_last_v1(arr, pos):
    """Recursive Function to check whether last index will reached or not."""
    if pos == len(arr) - 1:
        return True

    max_jump = min(pos + arr[pos], len(arr) - 1)

    for next_pos in range(pos + 1, max_jump + 1):
        if hop_to_last_v1(arr, next_pos):
            return True

    return False


seq = [3, 2, 2, 1, 1, 0]
print(hop_to_last_v1(seq, 0))
