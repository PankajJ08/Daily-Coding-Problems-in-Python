"""The power set of a set is the set of all its subsets.
Write a function that, given a set, generates its power set.

For example, given the set {1, 2, 3},
it should return {{}, {1}, {2}, {3}, {1, 2}, {1, 3}, {2, 3}, {1, 2, 3}}."""


def power_set(sets, size):
    """Function to generate power-set of a given set."""
    ps_size = 1 << size
    p_set = ["" for _ in range(ps_size)]

    for i in range(ps_size):
        for j in range(size):

            if i & 1 << j:
                p_set[i] += sets[j]

    return p_set


set1 = [str(i) for i in range(5)]
print(power_set(set1, len(set1)))
