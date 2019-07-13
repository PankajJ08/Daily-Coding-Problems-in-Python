"""Let's define a "sevenish" number to be one which is either a power of 7,
or the sum of unique powers of 7. The first few sevenish numbers are 1, 7, 8, 49,
 and so on. Create an algorithm to find the nth sevenish number."""


def sevenish(n):
    if n < 1:
        raise Exception("Invalid value.")

    sevenish_arr = []
    power = 0

    while len(sevenish_arr) != n:
        y = 7 ** power
        temp = [y]

        for i in sevenish_arr:
            if len(sevenish_arr) + len(temp) == n:
                return temp[-1]

            temp.append(i + y)

        sevenish_arr += temp
        power += 1

    return sevenish_arr[-1]


num = 420
print(sevenish(num))
