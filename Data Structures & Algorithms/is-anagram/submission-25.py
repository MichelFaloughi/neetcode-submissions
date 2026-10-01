class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        return sorted(s) == sorted(t)

        from collections import defaultdict

        countS, countT = defaultdict(int), defaultdict(int)
        for i in range(len(s)): # or len(t), equivalent
            countS[s[i]] += 1
            countT[t[i]] += 1
        
        return countS == countT