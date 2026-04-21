class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        currMax = arr[-1]
        arr[-1] = -1

        for i in reversed(range(0, len(arr) - 1)): # range(0, len(arr) - 1, -1)
            temp = arr[i]
            arr[i] = currMax
            currMax = max(currMax, temp)

        return arr
    
        # [ 2, 4, 5, 3, 1, 2 ]
        # [                  ]



        