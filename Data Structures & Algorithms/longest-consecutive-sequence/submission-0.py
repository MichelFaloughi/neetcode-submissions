class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        # {2, 20, 4, 10, 3, 4, 5}
        # {1, 2, 3, 4, 5, 6, 7, 8}

        maxL = 0
        nums = set(nums)
        for num in nums:
          if num-1 in nums:
              continue
          else: # might be the start of a sequence
              temp, currL = num, 0
              while temp in nums:
                  currL += 1
                  temp += 1
              maxL = max(maxL, currL)
        
        return maxL

# learnings:
# - think of sorting too