class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # for num in nums
        # comp = target - nums[i]
        # check if you already say the comp
        #   if so, return indices
        #   if not, add num to dict
        # keep going

        # return [-1, -1]

        elem_to_idx = {} # num -> idx

        for i, num in enumerate(nums): # TODO: num, i
            comp = target - num

            if comp in elem_to_idx:
                return [
                    elem_to_idx[comp],
                    i
                ]
            elem_to_idx[num] = i
        
        return [-1, -1]









                
