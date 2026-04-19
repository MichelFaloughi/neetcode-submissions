class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r)//2

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return l+1 if nums[l] < target else l


    

    # [ -1, 0, 2, 4, 6, 8 ]
    # l        m        r
