"""Given a string with repeated characters, rearrange the string so that no two
adjacent characters are the same. If this is not possible, return None.

For example, given "aaabbc", you could return "ababac". Given "aaab", return None."""
from collections import defaultdict


def no_same_char(string):
    ans = ""

    store = defaultdict(int)
    for i in string:
        store[i] += 1

    for j in store:
        if store[j]:
            if ans and j == ans[-1]:
                return None
            ans += j
            store[j] -= 1

    return ans


a = "aaab"
print(no_same_char(a))
