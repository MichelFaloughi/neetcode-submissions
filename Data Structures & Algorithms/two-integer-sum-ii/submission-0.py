class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # l,r pointers
        # while l < r
        # check if add to targert:
            # if yes, return '1-indexed' pointer
            # if no
                # if too small, increase l by 1
                # if too big, decrease r by 1

        # return []
        
        l, r = 0, len(numbers) - 1
        
        while l < r:
            curr_num = numbers[l] + numbers[r]
            if curr_num == target:
                return [l+1, r+1]
            elif curr_num < target:
                l += 1
            else: # curr_num > target:
                r -= 1
        
        return []