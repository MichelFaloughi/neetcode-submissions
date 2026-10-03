class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # init freq dict ( num -> freq )
        # go through nums
        # populate freq dict
        # sort freq dict by k.value for v in freq dict
        # return that list[:k]

        from collections import defaultdict
        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        tuples_list = [(k,v) for k, v in freq.items()]
        sorted_tuples = sorted(tuples_list, key=lambda x: x[1], reverse=True)
        return [t[0] for t in sorted_tuples[:k]]