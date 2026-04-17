class Solution:
    def climbStairs(self, n: int) -> int:
        
        # ways to climb from step n, 1
        # ways to climb from step n-1, 1

        # 1 - 2 - 3 - 4 - 5
        #             o   t
        #   1 - 2
        # n
        one, two = 1, 1

        for _ in range(n-1):
            one, two = one + two, one
        
        return one
