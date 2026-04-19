class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # [ 1, 2, 1, 2, 1, 1, 1 ]
        cache = [None for _ in range(len(cost))]

        def search(i):
            
            if i >= len(cost):
                return 0
            
            if cache[i]:
                return cache[i]

            cache[i] = cost[i] + min(search(i+1),  search(i+2))
            return cache[i]
        
        return min(search(0), search(1))



        