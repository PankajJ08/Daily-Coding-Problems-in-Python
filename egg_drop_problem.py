"""You are given N identical eggs and access to a building with k floors.
Your task is to find the lowest floor that will cause an egg to break,
if dropped from that floor. Once an egg breaks, it cannot be dropped again.
If an egg breaks when dropped from the xth floor, you can assume it will also break
when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take,
in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor,
beginning with the first, until we reach the fifth floor, so our solution will be 5."""
import sys
sys.setrecursionlimit(10000)


def recursive_solution(n, k):
    """Recursive Solution to solve the problem with n eggs, and k floors.
    where d is the number of drops(try)."""
    if n == 1:
        return k
    if k == 1 or k == 0:
        return k

    drops = []
    for i in range(1, k + 1):
        drops.append(max(recursive_solution(n - 1, i - 1), recursive_solution(n, k - i)))

    return 1 + min(drops)


def memoization_solution(n, k):
    """Solving the problem using top-down Dynamic Programming."""
    crate = [[-1 for _ in range(k + 1)]
             for _ in range(n)]

    for egg in range(n):
        crate[egg][0] = 0
        crate[egg][1] = 1

    for floor in range(1, k + 1):
        crate[0][floor] = floor

    return helping_memoization(n - 1, k, crate)


def helping_memoization(n, k, dp):
    drops = []
    if dp[n][k] != -1:
        return dp[n][k]

    else:
        for i in range(2, k + 1):
            drops.append(max(helping_memoization(n - 1, i - 1, dp),
                             helping_memoization(n, k - i, dp)))

        dp[n][k] = 1 + min(drops)
        return dp[n][k]


def bottom_up_dp(n, k):
    crate = [[-1 for _ in range(k + 1)]
             for _ in range(n)]

    for egg in range(n):
        crate[egg][1] = 1
        crate[egg][0] = 0

    for floor in range(k + 1):
        crate[0][floor] = floor

    for x in range(1, n):
        for y in range(2, k + 1):
            drops = []
            for z in range(2, y + 1):
                drops.append(max(crate[x - 1][z - 1], crate[x][y - z]))
            crate[x][y] = 1 + min(drops)

    return crate[n - 1][k]


N = 3
K = 100
# print(recursive_solution(N, K))
# print(memoization_solution(N, K))
print(bottom_up_dp(N, K))
