class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        maxL, l, r = 0, 0, 0
        idx = {}

        while r < len(s):
            if s[r] in idx and idx[s[r]] >= l:
                l = idx[s[r]] + 1
                # for k in list(idx.keys()):
                #     if idx[k] < l:
                #         idx.pop(k)
            
            idx[s[r]] = r
            currL = r - l + 1
            maxL = max(maxL, currL)
            r += 1

        return maxL