class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        # keep track of what you've seen in a ds
        s = set([i for i in range(0, len(nums) + 1)])

        for num in nums:
            s.remove(num)

        return list(s)[0]