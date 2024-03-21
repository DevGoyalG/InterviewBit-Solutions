# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @return a list of Interval
    def merge(self, intervals):
        if not intervals:
            return []

        intervals.sort(key=lambda x: x.start)

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            current_interval = intervals[i]
            last_merged_interval = merged_intervals[-1]

            if current_interval.start <= last_merged_interval.end:
                last_merged_interval.end = max(last_merged_interval.end, current_interval.end)
            else:
                merged_intervals.append(current_interval)

        return merged_intervals
