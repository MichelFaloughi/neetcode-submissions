class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        # [ 1, 2, 3, 3 ]
        return len(nums) != len(set(nums))
        