class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        res = [[1]]

        for i in range(1, rowIndex + 1): # TODO: maybe + 1

            next_row = [0] * (i + 1)
            prev_row = res[i-1]
            
            for j in range(len(prev_row)): # the previous row

                next_row[j]     += prev_row[j]
                next_row[j+1]   += prev_row[j]
            
            res.append(next_row)

        return res[-1]
    # [ 1, 3, 3, 1 ]
    # [ 1, 4, 6, 4, 1 ]


    # TODO: what if rowIndex = 0

