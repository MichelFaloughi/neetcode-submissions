class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)

        total = sum([i for i in range(n + 1)])
        
        return total - sum(nums)





        
        