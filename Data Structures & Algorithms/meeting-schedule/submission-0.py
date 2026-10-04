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
        # -------
        #      ---------------------------
        #               ------
        #                   -------

        # sort intervals by start time ascending
        intervals.sort(key=lambda i:i.start)

        for i in range(len(intervals) - 1):
            if intervals[i].end > intervals[i + 1].start:
                return False
        return True

        # for i in range(len(intervals) - 1):
        #   check if intervals[i].end > intervls[i+1].start
        #       return False
        # return True if we survive the loop

        






        def clash(i1:Intervarl, i2:Intervarl) -> bool:
            pass
        # how can i1 and i2 clash ? 
        # i1.end > i2.start and i2.end > i1.start

        #                - - - - - - - - 
        #                    - - - - 