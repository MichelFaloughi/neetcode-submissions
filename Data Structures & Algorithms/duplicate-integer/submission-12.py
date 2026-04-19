class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        from collections import defaultdict

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
            if freq[num] > 1:
                return True
        
        return False
        