"""Snakes and Ladders is a game played on a 10 x 10 board,
the goal of which is get from square 1 to square 100.
On each turn players will roll a six-sided die and move forward
a number of spaces equal to the result. If they land on a square that represents
a snake or ladder, they will be transported ahead or behind, respectively, to a new square.

Find the smallest number of turns it takes to play snakes and ladders.

For convenience, here are the squares representing snakes and ladders, and their outcomes:

snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}"""
from collections import deque


class QueueInfo:
    def __init__(self, vertex=0, distance=0):
        self.v = vertex
        self.d = distance

    def __str__(self):
        return "Value: {0} and Distance: {1}".format(self.v, self.d)


def get_in_dice(move, n):
    queue = deque()
    queue.append(QueueInfo(0, 0))
    visited = [False] * n
    visited[0] = True
    q = QueueInfo()
    while queue:
        q = queue.popleft()
        vertex = q.v

        if vertex == n-1:
            break

        i = vertex + 1

        while i <= vertex+6 and i < n:
            if not visited[i]:
                a = QueueInfo()
                a.d = q.d + 1
                visited[i] = True

                if move[i] != -1:
                    a.v = move[i]

                else:
                    a.v = i
                queue.append(a)

            i += 1

    return q.d


cells = 101
snakes = {16: 6, 48: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}
moves = [-1] * cells
for x in snakes:
    moves[x] = snakes[x]

for y in ladders:
    moves[y] = ladders[y]

print(get_in_dice(moves, cells))
