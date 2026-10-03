class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {} # key (sorted str) -> List[str]

        from collections import defaultdict
        res = defaultdict(list)

        for s in strs:
            res["".join(sorted(s))].append(s)
        
        return list(v for v in res.values())