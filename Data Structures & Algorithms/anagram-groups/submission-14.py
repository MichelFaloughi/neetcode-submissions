class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ["act","pots","tops","cat","stop","hat"]
        #   ^

        # res = {} same letters -> same list
        
        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            hsh = defaultdict(int) # letter -> count
            for c in s:
                hsh[c] += 1
            key = frozenset(hsh.items())
            res[key].append(s)
        
        return list(res.values())

