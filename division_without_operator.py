"""Implement division of two positive integers without using
the division, multiplication, or modulus operators.
Return the quotient as an integer, ignoring the remainder."""


def find_sign(num, din):
    """Function that return -ve sign if any of the numbers is -ve and
    return absolute values of numbers."""
    sign = 1

    if num < 0:
        sign = -sign
        num = -num
    if din < 0:
        sign = -sign
        din = -din

    return sign, num, din


def solution_v1(num, din):
    """Function to divide using successive subtraction."""
    sign, num, din = find_sign(num, din)
    quo = 0

    while num >= din:
        num -= din
        quo += 1

    rem = num
    s_quo = sign * quo

    return s_quo, rem


def solution_v2(num, din):
    """Function to perform division using bitwise operation."""
    sign, num, din = find_sign(num, din)
    temp = 0
    quo = 0

    for i in range(31, -1, -1):
        if num >= temp + (din << i):
            temp += din << i
            quo |= 1 << i

    s_quo = sign * quo
    rem = num - temp

    return s_quo, rem


x, y = solution_v2(10**50, 7)
print("Quotient = {} and Reminder = {}".format(x, y))
