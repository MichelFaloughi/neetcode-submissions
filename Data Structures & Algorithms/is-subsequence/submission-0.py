class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # a b c d e
        # j

        # a c e
        #       i

        # assuming len(s) <= len(t)
        # think about when s and t are ''

        i, j = 0, 0

        while i < len(s) and j < len(t):

            if t[j] == s[i]: # there is a match
                i += 1
                j += 1
            else:
                j += 1
        
        return i >= len(s)




        