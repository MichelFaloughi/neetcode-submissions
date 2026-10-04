"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        # [ i1, i2, i3, i4 ]
        #           
        #  ----------
        #              ------------
        #                       -------

        # sort by start time
        # for each pair of intervals, check if i1 end > i2 start

        intervals.sort(key=lambda i:i.start) # O(n log n)

        for i in range(len(intervals) - 1):
            j = i + 1
            if intervals[i].end > intervals[j].start:
                return False
        
        return True
        