"""You come across a dictionary of sorted words in a language you've never seen before.
Write a program that returns the correct order of letters in this language.

For example, given ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz'],
you should return ['x', 'z', 'w', 'y']."""
from collections import defaultdict


def alien_lang(words):
    graph = defaultdict(list)

    for i in range(len(words) - 1):
        k = 0
        first_word = words[i]
        second_word = words[i + 1]

        while k < min(len(first_word), len(second_word)):
            if second_word[k] not in graph:
                graph.setdefault(second_word[k], [])

            if first_word[k] != second_word[k]:
                graph[first_word[k]].append(second_word[k])
                break

            k += 1

    return topological_sort(graph)

def dfs_topsort(graph, stack, visited, vertex):
    for v in graph[vertex]:
        if v not in visited:
            visited.append(v)
            dfs_topsort(graph, stack, visited, v)

    stack.insert(0, vertex)


def topological_sort(graph):
    stack = []
    visited = []
    for vertex in graph:
        if vertex not in visited:
            visited.append(vertex)
            dfs_topsort(graph, stack, visited, vertex)

    return stack


lang = ['xww', 'wxyz', 'wxyw', 'ywx', 'ywz']
print(alien_lang(lang))
