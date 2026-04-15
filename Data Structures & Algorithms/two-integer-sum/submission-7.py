class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        comps_to_index = {nums[0]: 0}

        for i in range(1, len(nums)):
            comp = target - nums[i]
            if comp in comps_to_index:
                return [comps_to_index[comp], i]
            else:
                comps_to_index[nums[i]] = i
        return []