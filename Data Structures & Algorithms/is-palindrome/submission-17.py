class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 'a n b n a'
        #      l
        #      r
        
        l, r = 0, len(s) - 1
        while l < r: # TODO: check if <= 
            
            while l < r and not s[l].isalnum():
                l+=1
            while l < r and not s[r].isalnum():
                r-=1
            
            if l < r:
                if s[l].lower() == s[r].lower():
                    l += 1
                    r -= 1
                else:
                    return False
        return True