class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # [3, 4, 5, 6], target = 7
        idx = {}

        # loop through nums
        # if comp in idx, return both
        # register num in idx and keep going

        for i, num in enumerate(nums):
            comp = target - num
            if comp in idx:
                return [idx[comp], i]
            idx[num] = i
        
        return [-1, -1]


# assumptions:
# is list elems unique ? yes 
# [3, 4, 5, 6], target = 7
#  l        r


                
