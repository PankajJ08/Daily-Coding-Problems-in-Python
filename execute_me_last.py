"""---- Josephus Problem ----

There are N prisoners standing in a circle, waiting to be executed.
The executions are carried out starting with the kth person,
and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand
in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3],
so you should return 3.

Bonus: Find an O(log N) solution if k = 2."""
import math


def last_man_standing(n, k):
    if n == 1:
        return 1

    return (last_man_standing(n - 1, k) + (k-1)) % n + 1


def last_man_standing_iteratively(n, k):
    p = 1
    for i in range(2, n + 1):
        p = (p + k - 1) % i + 1

    return p


def josephus_problem(n):
    """Method to solve a special case when k = 2.
    The recurrence is given by:
    f(n) = 2f(n/2) + 1      ---- for n is even.
    f(n) = 2f(n-1 /2) + 1   ---- for n is odd.
    It is solvable by f(n) = 2L + 1 where L = n - 2 ^ floor(log n)."""

    # if n == 1:
    #     return 1
    #
    # return 2 * (n - 2 ** math.floor(math.log2(n))) + 1

    p = 1
    for i in range(2, n + 1):
        p = 2 * (i - 2 ** math.floor(math.log2(i))) + 1

    return p


def most_significant_bit(n):
    a = 0
    while n != 1:
        n >>= 1
        a += 1
    return a


def bitwise_jp_solution(n):
    """X = n - 2^a
    ans = 2X + 1"""
    a = most_significant_bit(n)
    x = n ^ (1 << a)
    ans = (x << 1) | 1

    return ans


N = 500
K = 2
# print(last_man_standing(N, K))
print(last_man_standing_iteratively(N, K))
print(josephus_problem(N))
print(bitwise_jp_solution(N))
