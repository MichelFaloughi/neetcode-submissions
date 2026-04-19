class Solution:
    def generate(self, numRows: int) -> List[List[int]]:

        res = []

        for i in range(numRows):

            row = [1] * (i+1)

            if len(res) > 1: # there is a previous row

                for j in range(1, i):
                
                    row[j] = res[i - 1][j - 1] + res[i - 1][j]
            res.append(row)
        
        return res
                

                #  [ 1, 3, 3, 1 ]
                # [ 1, 4, 6, 4, 1 ]
        