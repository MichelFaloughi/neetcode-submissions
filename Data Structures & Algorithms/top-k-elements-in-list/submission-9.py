class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # sort by freq
        # add k in a list and retrun it

        from collections import defaultdict
        freq = defaultdict(int) # elem -> freq
        for n in nums:
            freq[n] += 1
        
        freq = sorted(freq, key=lambda n:freq[n], reverse=True)

        return freq[:k]

