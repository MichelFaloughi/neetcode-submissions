class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        # [ 1, 2, 3, 4, 5, 3, 6, 7, 8, 9 ]
        seen = set()

        for num in nums:
            if num not in seen: #TODO: maybe 'not (num in seen)'
                seen.add(num)
            else:
                return True
        
        return False
