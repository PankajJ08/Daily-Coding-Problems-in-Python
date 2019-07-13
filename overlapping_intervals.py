"""Given a list of possibly overlapping intervals,
return a new list of intervals where all overlapping intervals have been merged."""


class Intervals:
    """class of intervals having start and end point."""
    def __init__(self, s=0, e=0):
        """Initializer method for Intervals."""
        self.start = s
        self.end = e

    def __repr__(self):
        """Function to return a list with start and end points."""
        return "[{}, {}]".format(self.start, self.end)


class Solution:
    """class to find a overlapping intervals."""
    def merge(self, intervals):
        intervals = sorted(intervals, key=lambda x: x.start)
        out = []

        for i in intervals:
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out.append(i)

        return out


interval = [Intervals(1, 2), Intervals(6, 11), Intervals(0, 5), Intervals(7, 9), Intervals(1, 2)]
print(Solution().merge(interval))
