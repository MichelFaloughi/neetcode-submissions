class Solution:
    def rob(self, nums: List[int]) -> int:
        
        i, cache = 0, [-1 for _ in range(len(nums))]

        def helper(i):
            
            if i >= len(nums):
                return 0

            if cache[i] != -1: # then we have a cached value
                return cache[i]
            
            if i >= len(nums) - 2: 
                return nums[i]

            cache[i] = nums[i] + max(helper(i+2), helper(i+3))
            return cache[i]

        return max(helper(0), helper(1))
            
        # [4, 7, 2, 9, 3, 5]
        #           ^
        #     ^
        # [4, 7, 6, 16, 10, 21]




        