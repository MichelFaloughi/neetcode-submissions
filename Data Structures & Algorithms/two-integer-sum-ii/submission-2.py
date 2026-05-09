class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # [ 1, 2, 2, 3, 4, 6, 8 ], target = 3
        #   l                 r


        # caveats:
        # - 1-indexed           just add 1 to the answer indices
        # - index1 != index2    contrain l < r

        l, r = 0, len(numbers) - 1

        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            elif numbers[l] + numbers[r] > target:
                r -= 1
            else: # numbers[l] + numbers[r] < target:
                l += 1
        
        return [-1, -1]
