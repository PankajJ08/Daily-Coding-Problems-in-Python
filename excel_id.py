"""Given a column number, return its alphabetical column id.
For example, given 1, return "A". Given 27, return "AA"."""


def return_id(num, char_set):
    "Function that return the column id of a given number."
    ans = ""
    while num:
        a = num % 26
        num //= 26
        ans += char_set[a - 1]
    return ans[::-1]


charset = [chr(i) for i in range(65, 91)]
n = 100000767
print(return_id(n, charset))
