class Solution:
    # def isPalindrome(self, s: str) -> bool:
    #     l, r = 0, len(s) - 1

    #     while l < r:
    #         while l < r and not s[l].isalnum():
    #             l += 1
    #         while l < r and not s[r].isalnum():
    #             r -= 1

    #         if s[l].lower() != s[r].lower():
    #             return False
    #         l += 1
    #         r -= 1

    #     return True

    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for letter in s:
            if letter.isalnum():
                new_s += letter.lower()
        
        return new_s == new_s[::-1]
# learnings:
# - there is the two pointer approach ( better, O(n) time and O(1) space)
# - there is the reverse string approach ( worse, O(n) time and O(n) space)