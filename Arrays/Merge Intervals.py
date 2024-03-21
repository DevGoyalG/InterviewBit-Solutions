# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    # @param intervals, a list of Intervals
    # @param new_interval, a Interval
    # @return a list of Interval
    def insert(self, intervals, new_interval):
        merged_intervals = []
        i = 0
        n = len(intervals)
        
        while i < n and intervals[i].end < new_interval.start:
            merged_intervals.append(intervals[i])
            i += 1
        
        while i < n and intervals[i].start <= new_interval.end:
            new_interval.start = min(new_interval.start, intervals[i].start)
            new_interval.end = max(new_interval.end, intervals[i].end)
            i += 1
        
        merged_intervals.append(new_interval)
        
        while i < n:
            merged_intervals.append(intervals[i])
            i += 1
        
        return merged_intervals
