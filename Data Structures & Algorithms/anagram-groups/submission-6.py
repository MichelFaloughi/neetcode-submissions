from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # init a defaultdict
        d = defaultdict(list) # letters to list

        for s in strs:
            key = tuple(sorted(s))
            d[key].append(s)
        return list(d.values())
