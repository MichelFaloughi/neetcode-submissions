class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        maxW, l, r = 0, 0, len(heights) - 1
        while l < r:
            # math
            currW = (r - l) * min(heights[r], heights[l])
            maxW = max(currW, maxW)

            # increment
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
        
        return maxW






