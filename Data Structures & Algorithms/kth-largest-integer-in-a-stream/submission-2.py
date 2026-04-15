from heapq import heapify, heappop, heappush

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # have a minHeap, pop until its size is k
        # the min will be the kth largest
        self.k, self.minHeap = k, nums
        heapq.heapify(self.minHeap)

        while len(self.minHeap) > self.k: # watch off by one
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        """
        return the kth largest, THEN we add ???
        """
        
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k: # watch off by one
            heapq.heappop(self.minHeap)

        return self.minHeap[0]
        


# Input:
# ["KthLargest", [3, [1, 2, 3, 3]], "add", [3], "add", [5], "add", [6], "add", [7], "add", [8]]

# Output:
# [null,                             3,          3,          3,          5,          6]

#                                                            [1,2,3,3,3,5,6]