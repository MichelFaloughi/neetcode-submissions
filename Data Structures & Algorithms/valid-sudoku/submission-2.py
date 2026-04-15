from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set) # row_num to set
        cols = defaultdict(set) # col_num to set
        boxs = defaultdict(set) # box_tuple to set

        # loop over every r and c, get val
        # skip if '.'
        # if rows[r].contains(val) or cols[c].contains(val) or boxs.contains(val)
            # return False
        # else add and keep going

        for r in range(len(board)):
            for c in range(len(board)):
                
                val = board[r][c]
                if val == '.':
                    continue
                    
                if val in rows[r] or val in cols[c] or val in boxs[(r//3, c//3)]:
                    return False
                else:
                    rows[r].add(val)
                    cols[c].add(val)
                    boxs[(r//3, c//3)].add(val)

        return True
