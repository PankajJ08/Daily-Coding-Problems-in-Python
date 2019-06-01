"""Given a list of integers and a number K,
return which contiguous elements of the list sum to K.

For example, if the list is [1, 2, 3, 4, 5] and K is 9,
then it should return [2, 3, 4]."""


def find_sum(arr, k):
    """Function to find the contiguous sum using dictionary."""
    dic = {}
    pre_sum = 0

    for i in range(len(arr)):
        pre_sum += arr[i]

        if pre_sum == k:
            return [arr[x] for x in range(i + 1)]

        temp = pre_sum - k

        if temp in dic:
            start = dic[temp] + 1
            return [arr[x] for x in range(start, i + 1)]

        dic[pre_sum] = i

    return "Solution not exist!"


seq = [5, 7, 2, 6, 8]
print(find_sum(seq, 15))
