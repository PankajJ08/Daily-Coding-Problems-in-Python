""" There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N,
write a function that returns the number of unique ways you can climb the staircase.
The order of the steps matters.
"""


# By dynamic programming in (O(2*N)) running time.
def num_ways(n):
    if n == 0 or n == 1:
        return 1
    num = [1, 1]
    for i in range(2, n + 1):
        num.append(num[i - 1] + num[i - 2])
    return num[n]


# By recursive way with (O(2^N)) running time.
def ways(n):
    if n == 0 or n == 1:
        return 1
    else:
        return ways(n - 1) + ways(n - 2)


c = int(input("Enter no. of Steps: "))
steps = num_ways(c)
print("Ways to climb the staircase: {}".format(steps))
