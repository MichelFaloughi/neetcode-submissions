from heapq import heappush, heappop, heapify
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k , self.minHeap = k, nums
        heapify(self.minHeap)              # O(n)

        while len(self.minHeap) > self.k:
            heappop(self.minHeap)
            

        # now self.minHeap has k values
         

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)

        return self.minHeap[0]
        





# [ 1, 2, 3, 3, 4, 5, 6, 6, 6, 7, 8, 9 ], k = 4
#  