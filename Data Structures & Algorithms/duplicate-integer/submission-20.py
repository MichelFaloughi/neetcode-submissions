class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # loop until find duplicate return True
        # if loop ends without returning, return fale
        
        # init empty freq dict
        # for num in nums
        # check if num in freq dict keys
        #   return True
        # else add the entry with, say, freq[num] = 1

        # return False (if loop ended without returning true
        
        
        # ALTERNATIVE SOLUTION
        return len(nums) != len(set(nums))
        