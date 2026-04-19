class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l, r = 0, len(nums) - 1

        while l < r:
            m = (l+r) // 2
            if nums[m] > nums[r]: # min is in right half
                l = m + 1
            else: # nums[m] <= nums[r]
                r = m
        
        return nums[l] # or nums[r] but NOT nums[m]





        # THIS IS O(n) !!
        # i = len(nums) - 1
        # j = i - 1

        # while j >= 0:
        #     if nums[j] > nums[i]:
        #         return nums[i]
        #     j -= 1
        #     i -=1

        # return nums[0] # if j < 0


        # [ 3, 4, 5, 6, 1, 2 ]
        #   l           m  r
        #
        #
        #
        # [ 4, 5, 0, 1, 2, 3 ]
        #   l        m     r
        #
        #
        #
        #
        # [ 4, 5, 6, 7 ]

