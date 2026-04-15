class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # max heapify
        # while stones has at least 2 stones
        # pop the first, peek at the second and store it's value
        # if peeked == popped and len(stones) > 2 still (in terms of value), then pop the peeked too
        # 

        stones = [-s for s in stones] # O(n)
        heapq.heapify(stones) #

        while len(stones) >= 2: # we have at least 3, can afford to smash two
            s1 = heapq.heappop(stones)
            s2 = heapq.heappop(stones)

            if s1 == s2: # there will still be a stone to return
                continue
            else:
                s2 = s1 - s2 # we KNOW s2 > 0 thanks to maxHeap
                heapq.heappush(stones, s2)
                
        
        return 0 if len(stones) == 0 else -stones[0]

        