"""We say a number is sparse if there are no adjacent ones in its binary representation.
For example, 21 (10101) is sparse, but 22 (10110) is not.
For a given input N, find the smallest sparse number greater than or equal to N."""


def binary_to_decimal(num):
    ans = 0
    j = len(num) - 1
    for i in num:
        ans += int(i) * 1 << j
        j -= 1

    return ans


def decimal_to_binary(num):
    ans = 0
    i = 1
    while num:
        ans += (num & 1) * i
        num >>= 1
        i *= 10

    return ans


def check_sparse(num):
    """Function to check whether a number is sparse or not."""
    if num & (num >> 1):
        return False

    return True


def find_next_sparse(num):
    """Function to return next sparse number."""
    temp = []
    while num:
        temp.append(num & 1)
        num >>= 1
    temp.append(0)

    final_p = 0
    for i in range(len(temp) - 1):
        if temp[i - 1] == 1 and temp[i] == 1 and temp[i + 1] != 1:
            temp[i + 1] = 1

            for j in range(i, final_p - 1, - 1):
                temp[j] = 0

            final_p = i + 1

    ans = 0
    for i in range(len(temp)):
        ans += temp[i] * (1 << i)

    return ans


n = 42
print(binary_to_decimal("1000011"))
print(decimal_to_binary(42))
print(find_next_sparse(n))
print(check_sparse(n))
