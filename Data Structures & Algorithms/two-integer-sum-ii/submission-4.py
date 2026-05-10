class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # [ 1, 2, 3, 4 ], target = 3
        #      l     r
        
        l, r = 0, len(numbers) - 1

        while l < r:
            currS = numbers[l] + numbers[r]
            if currS == target:
                return [l+1, r+1]
            elif currS > target:
                r -= 1
            else: # currS < target:
                l += 1
        
        return [-1, -1]

