class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # ["act","pots","tops","cat","stop","hat"]
        #   ^

        # res = {} same letters -> same list
        
        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            res[key].append(s)
        
        return list(res.values())

