from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = defaultdict(list) # str to list

        for elem in strs:
            anags[str(sorted(elem))].append(elem)
            
        return list(anags.values())

# how to handle duplicates ? tops tops in strs, for example