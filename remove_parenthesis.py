"""Given a string of parentheses, write a function to compute
the minimum number of parentheses to be removed to make the string valid
(i.e. each open parenthesis is eventually closed)."""

from collections import deque


def remove_paren(str):
    count = 0
    stack = deque()
    for i in str:
        if i == '(':
            stack.append(i)
            count += 1
        if i == ')':
            if stack:
                stack.popleft()
                count -= 1
            else:
                count += 1
    return count


str = input("Enter a string: ")
print(remove_paren(str))
