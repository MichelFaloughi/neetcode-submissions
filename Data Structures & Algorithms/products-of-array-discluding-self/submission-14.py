class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        prod, zeros = 1, 0

        for num in nums:
            if num: # check if not a 0
                prod *= num
            else:
                zeros += 1
        
        if zeros > 1: return [0] * len(nums)

        res = []
        if zeros == 1: return [0 if num != 0 else prod for num in nums]
        
        else: return [int(prod/num) for num in nums]
        
        