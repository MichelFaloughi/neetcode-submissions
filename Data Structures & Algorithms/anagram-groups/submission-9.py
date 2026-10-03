class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            hsh = defaultdict(int)
            for c in s:
                hsh[c] +=1
            res[frozenset(hsh.items())].append(s)
        
        return list(v for v in res.values())