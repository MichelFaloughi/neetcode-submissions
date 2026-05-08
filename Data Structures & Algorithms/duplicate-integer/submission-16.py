class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # return len(nums) != len(set(nums))
        # [ 1, 2, 3, 4, 5, 3, 6, 7, 8, 9, 10, 11 ]
        
        freq = {} # int -> 1

        for num in nums:
            if num in freq: #TODO: make sure 'in freq' means in keys
                return True
            freq[num] = 1
        
        return False
        