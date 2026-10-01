class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        freq = {}

        for num in nums:
            if num in freq: # this checks the keys
                return True
            
            freq[num] = 1
        
        return False
        
        
        # ALTERNATIVE SOLUTION
        # return len(nums) != len(set(nums))
        