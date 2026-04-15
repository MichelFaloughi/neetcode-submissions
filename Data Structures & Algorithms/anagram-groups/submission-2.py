class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anags = {} # str to list

        for elem in strs:
            if str(sorted(elem)) in anags:
                anags[str(sorted(elem))].append(elem)
            else:
                anags[str(sorted(elem))] = [elem]
        
        return list(anags.values())

# how to handle duplicates ? tops tops in strs, for example