class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        # [3, 4, 5, 6], target = 7
        #  l  r

        # brute force -> O(n^2)
        
        # sorting, O(n log n)
        # search,  O(log n)


        # brute force

        # init l, r
        # while l not end idx
        # r = 1 + 1
        # while r not end ix
        # check sum , satisfies return
        # else r += 1

        l = 0
        
        while l < len(nums) - 1: 
            r = l + 1
            while r <= len(nums) - 1: # TODO: if breaks, check OBO
                if nums[l] + nums[r] == target:
                    return [l, r]
                r += 1
            l += 1
        
        return [-1, -1]

# assumptions:
# is list elems unique ? 
                
