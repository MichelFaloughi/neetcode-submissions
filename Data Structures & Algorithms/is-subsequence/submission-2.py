class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # RECURSION
        if s == '' or t == '':
            return s == '' 
        
        elif s[0] == t[0]:
            return self.isSubsequence(s[1:], t[1:])
        
        else:
            return self.isSubsequence(s, t[1:]) 
            # don't have to make a copy, takes O(n) times












        # TWO POINTERS
        # i, j = 0, 0

        # while i < len(s) and j < len(t):

        #     if t[j] == s[i]: # there is a match
        #         i += 1
        #         j += 1
        #     else:
        #         j += 1
        
        # return i >= len(s)




        