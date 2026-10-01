class Solution:
    def isPalindrome(self, s: str) -> bool:

    # "@#$(Was it a car or a cat I saw?"
    #.          l                 r

    # init l, r = 0, len(s) - 1
    # loop while l < r
    # loop while l<r and not s[l].isalnum():
    # same with r
    # compare s[l] and s[r]
    #   early stop if !=
    #   else, keep goin
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