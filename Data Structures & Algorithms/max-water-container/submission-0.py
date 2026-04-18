class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        # assuming l < r
        # given two indices l, r
        # take h = min(l,r), w = r - l, wtr = h * w
        # 
        
        maxWater = 0
        l, r = 0, len(heights) - 1

        while l < r:
            currWater = min(heights[l], heights[r]) * (r - l) # height * width
            maxWater = max(maxWater, currWater)

            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
        return maxWater

