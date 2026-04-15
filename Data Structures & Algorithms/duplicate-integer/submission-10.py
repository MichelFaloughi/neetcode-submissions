class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return not len(nums) == len(set(nums))

# learnings:
# - if num in frequency_dict, is better than if num in list(frequency_dict.keys())
#   because hash lookups are O(1) on average

# other, more verbose solution:
# frequency_dict = {}
        
#         for num in nums:

#             if num in frequency_dict:
#                 return True
#             else:
#                 frequency_dict[num] = 1
#         return False
