class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        # [ -1, 0, 1, 2, -1, -4 ], target = 0
        # [ -4, -1, -1, 0, 1, 2, 2 ], target = 0
        #    i       l           r

        nums.sort()
        res = [] 

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]: # skip duplicate i's
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    res.append([nums[i], nums[l], nums[r]])

                    # TODO: smart increment l
                    temp = nums[l]
                    while l < len(nums) and nums[l] == temp:
                        l += 1

                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else: # nums[i] + nums[l] + nums[r] < 0:
                    l += 1
        
        return res


        # loop through len(nums) - 2
        # set l,r as i + 1, len(nums) - 1
        # while l < r
        # compare num + nums[l] + nums[r] to 0 if too big/small dec/inc, if good add to res
        # if match, increment l while l != previous l
        


