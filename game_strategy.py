"""You are asked to play the following game. You and an opponent take turns choosing either
the first or last coin from the row, removing from the row, and receiving the value of the coin.

Write a program that returns the maximum amount of money you can win with certainty,
if you move first, assuming your opponent plays optimally."""


def optimal_strategy(arr):
    n = len(arr)
    table = [["-" for _ in range(n)]
             for _ in range(n)]

    for spaces in range(n):
        for j in range(spaces, n):
            i = j - spaces

            x, y, z = 0, 0, 0

            if i + 2 <= j:
                x = table[i + 2][j]

            if i + 1 <= j - 1:
                y = table[i + 1][j - 1]

            if i <= j - 2:
                z = table[i][j - 2]

            table[i][j] = max(arr[i] + min(x, y), arr[j] + min(y, z))

    return table[0][n - 1]


values = [8, 15, 7, 1]
print(optimal_strategy(values))
