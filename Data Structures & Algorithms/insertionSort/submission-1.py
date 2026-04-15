# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        
        all_pairs = []

        for i in range(len(pairs)):
            temp_idx = i
            while temp_idx > 0 and pairs[temp_idx - 1].key > pairs[temp_idx].key:
                pairs[temp_idx], pairs[temp_idx - 1] = pairs[temp_idx - 1], pairs[temp_idx]
                temp_idx -= 1
                

            # add to list
            all_pairs.append(pairs[:])
        
        return all_pairs

        # [2, 6, 8, 4, 9, 4]
        # temp_pair = 4
        # 4 = 6
        # 6 = temp_pair
        