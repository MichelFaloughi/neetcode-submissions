class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #   [ 1, 2, 4, 6 ] -> [48, 24, 12, 8]
        #           ^

        #   left =  [ 1  2  8  48 1  ]
        #   right = [ 1  48 48 24 6  ]

        #   for i in range(len(nums)):
        #       nums[i] = left_to_right[i-1] * 
        #                 right_to_left[i+1]

        curr_num, left, right = 1, [], [1 for _ in range(len(nums))]
        n = len(nums)

        for num in nums: # O(n) time and space
            curr_num *= num
            left.append(curr_num) # appends to end of l

        curr_num = 1
        for i, num in enumerate(nums[::-1]):
            curr_num *= num
            right[n - 1 - i] = curr_num


        for i in range(n): # TODO: fix OOB
            if i == 0:
                nums[i] = 1 * right[i+1]
            elif i == n - 1:
                nums[i] = left[i-1] * 1
            else:
                nums[i] = left[i-1] * right[i+1]

        return nums