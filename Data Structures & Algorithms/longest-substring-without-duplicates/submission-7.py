class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        maxL, l, r = 0, 0, 0
        idx = {} # char -> idx

        while r < len(s):
            
            if s[r] in idx and idx[s[r]] >= l:
                l = idx[s[r]] + 1

            idx[s[r]] = r
            currL = r - l + 1
            maxL = max(maxL, currL)
            r += 1
        
        return maxL
            # 



       # " b x p z r y z x b c d "
       #.          l
       #.          r
        