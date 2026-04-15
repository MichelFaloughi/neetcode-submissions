class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxL = 0 # init
        l,r = 0,0
        seen = set()
        
        if s: # if not '' and > 1
            while r < len(s):
                if not s[r] in seen:
                    newL = r - l + 1 
                    maxL = max(newL, maxL) # update max
                    seen.add(s[r])
                    r += 1
                else:
                    newL -= 1
                    seen.remove(s[l])
                    l += 1
                    # don't update max, noway it increase from last time
        
        return maxL

        # 'z x y z a b c d'
        #.   l
        #.       r


# learnings:
# - newL = len(s[l:r]) + 1 works but r - l + 1 is cleaner and avoids creating a slice each iteration
