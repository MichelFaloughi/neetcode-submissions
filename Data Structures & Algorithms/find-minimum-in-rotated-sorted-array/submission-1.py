class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # loop from the top, keep track of elem that's ahead
        # compare elem and elem ahead, if elem ahead bigger, elem is min
        # if elem that's ahead index hits 0, that's the min

        i = len(nums) - 1
        j = i - 1

        while j >= 0:
            if nums[j] > nums[i]:
                return nums[i]
            j -= 1
            i -=1
        

        return nums[0] # if j < 0



        # [1, 2]
        # [2, 1]
        # [2, 3, 1]

        # [ 3, 4, 5, 6, 1, 2 ]
        #            j  i
        #
        #
        #
        # [ 4, 5, 0, 1, 2, 3 ]
        #            j  i
        #
        #
        #
        #
        # [ 4, 5, 6, 7 ]

