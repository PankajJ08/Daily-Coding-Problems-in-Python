"""Let X be a set of n intervals on the real line. We say that a set of points P "stabs" X
if every interval in X contains at least one point in P.
Compute the smallest set of points that stabs X.

For example, given the intervals [(1, 4), (4, 5), (7, 9), (9, 12)], you should return [4, 9]."""


def stab_the_num(intervals):
    """Solution using a greedy approach."""
    n = len(intervals)
    points = []

    left_points = []
    right_points = []
    for i, j in intervals:
        left_points.append(i)
        right_points.append(j)

    count = 0
    points.append(right_points[0])
    for i in range(1, n):
        if left_points[i] > points[count]:
            count += 1
            points.append(right_points[i])

    return points


inp = [(1, 4), (4, 5), (2, 9), (9, 12)]
print(stab_the_num(inp))
