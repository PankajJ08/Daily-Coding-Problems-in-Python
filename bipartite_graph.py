"""Given an undirected graph G, check whether it is bipartite.
Recall that a graph is bipartite if its vertices can be divided
into two independent sets, U and V,
such that no edge connects vertices of the same set."""

from collections import defaultdict, deque


def bipartite_check(g, s):
    """Check whether a graph is bipartite or not."""
    color = defaultdict(str)
    queue = deque()
    queue.append(s)
    color[s] = "Red"

    while queue:
        d = queue.pop()

        for i in g:
            for v in g[i]:
                if v == i:
                    return False

        for v in g[d]:
            if not color[v]:
                if color[d] == "Red":
                    color[v] = "Blue"
                else:
                    color[v] = "Red"

                queue.append(v)

            elif color[v] == color[d]:
                return False

    return True


g = {"a": ["b", "c"],
     "b": ["a", "d"],
     "c": ["a", "d"],
     "d": ["b", "c", "d"]
     }
print(bipartite_check(g, 'a'))
