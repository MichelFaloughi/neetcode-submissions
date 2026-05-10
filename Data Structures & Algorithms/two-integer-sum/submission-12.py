class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # [ 3, 4, 5, 6 ], target = 7

        # nums.sort()
        comps_to_idx = {} # int (comp) -> int (idx)

        for i, num in enumerate(nums):
            comp = target - num
            
            if comp in comps_to_idx:
                return [ comps_to_idx[comp] , i]
            
            comps_to_idx[num] = i 
        
        return [-1, -1]
        
        


