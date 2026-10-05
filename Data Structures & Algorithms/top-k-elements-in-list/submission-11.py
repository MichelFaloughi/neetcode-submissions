class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # build freq dict (num -> freq)
        # init empty heap, for num in dict^ keep pushing
        # while len(heap) > k, pop
        # size = len(heap)
        # return [pop()[1] for i in range(len(heap))]

        from collections import defaultdict
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        
        import heapq
        heap = []
        heapq.heapify([])

        for num in freq:
            heapq.heappush(heap, (freq[num], num))
        
        while len(heap) > k:
            heapq.heappop(heap)
        
        size = len(heap)

        return [heapq.heappop(heap)[1] for _ in range(size)]
        

        


