class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # two pointers at each end of array: l, r
        # if too small, increment l
        # if too big, decrement r
        
        l, r = 0, len(numbers) - 1

        while l < r:

            if numbers[l] + numbers[r] == target:
                return [l+1, r+1] # +1 bcz 1-indexed
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else: # numbers[l] + numbers[r] <= target:
                l +=1
        
        return []