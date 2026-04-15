from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        sorted_freq = sorted(freq, key=lambda x: freq[x], reverse=True)
        # sorted iterates over the keys, so the x in lambda x:... are the keys
        return sorted_freq[:k]