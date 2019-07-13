"""A number is considered perfect if its digits sum up to exactly 10.
Given a positive integer n, return the n-th perfect number.

For example, given 1, you should return 19. Given 2, you should return 28."""


def perfect_ten(n):
    """Function to return nth perfect number i.e. which digit sum up to exactly 10."""
    count = 0
    i = 19

    while i:
        sums = 0
        j = i

        while j > 0:
            sums += (j % 10)
            j //= 10

        if sums == 10:
            count += 1

        if n == count:
            return i

        i += 9


print(perfect_ten(1))
