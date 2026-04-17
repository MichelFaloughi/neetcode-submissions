class Solution:
    def climbStairs(self, n: int) -> int:
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        cache = [-1 for _ in range(n)]

        def helper(i):
            # base case
            if i >= n:
                return 1 if i==n else 0

            if cache[i] != -1:
                return cache[i]
            else:
                new_val = helper(i + 1) + helper(i+2)
                cache[i] = new_val
                return new_val

        return helper(0) # because i starts at 0


        # ways of reach n from 0 is 
        # ways of reaching n from 1 + ways of reaching n from 2
        
        # ways of reahcing n from 1 is
        # ways of reaching n from 2 + ways of reaching n from 3