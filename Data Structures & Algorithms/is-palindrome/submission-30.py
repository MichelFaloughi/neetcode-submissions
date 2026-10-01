class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        # init l, r = 0, len(s) - 1
        # loop while l < r
        #   try finding mistake
        #   while l < r and l.isalnum():
        #       l += 1
        #   while l < r and r.isalnum():
        #       r -= 1
        #   if s[l].lower() != s[r].lower():
        #       False
        #   l += 1
        #   r -= 1
        #
        # return True
        l, r = 0, len(s) - 1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l < r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True

# assumptions ' ' is not alnum
        