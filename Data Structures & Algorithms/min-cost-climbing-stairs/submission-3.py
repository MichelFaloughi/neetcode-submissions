class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # [ 1, 2, 1, 2, 1, 1, 1 ]
        cache = [None for _ in range(len(cost))]

        def search(i, cost):
            
            if i >= len(cost):
                return 0
            
            if i == len(cost) - 1 or i == len(cost) - 2:
                return cost[i]

            path1 = cache[i+1] if cache[i+1] else search(i+1, cost)  # path if took 1 step
            path2 = cache[i+2] if cache[i+2] else search(i+2, cost) # path if took 2 steps

            res = cost[i] + min(path1,  path2)
            cache[i] = res
            return res
        
        return min(search(0, cost), search(1, cost))



        