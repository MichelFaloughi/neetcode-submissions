class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # STEP 1 - Find relevant row via two pointers
        l, r = [0, len(matrix[0]) - 1], [len(matrix) - 1, 0]

        while l[0] < r[0]: 

            if matrix[l[0]][l[1]] < target:
                l[0] += 1
            if matrix[r[0]][r[1]] > target:
                r[0] -= 1
        
        # Assuming l and r are on the correct row
        # TODO: verify assumption
        # STEP 2 - Found row, now find target via binary search
        l[1], r[1] = 0, len(matrix[0]) - 1

        while l[1] <= r[1]:
            mid = [ l[0], (l[1] + r[1]) // 2 ]
            
            if matrix[mid[0]][mid[1]] == target:
                return True

            elif matrix[mid[0]][mid[1]] < target:
                l[1] = mid[1] + 1 # TODO: + 1 ?

            else: # matrix[mid[0], mid[1]] <= target:
                r[1] = mid[1] - 1 # TODO: - 1 ?
        
        print('l: ', l)
        print('r: ', r)
        #print('mid', m)
        return False


        
        # [
        #     [ 1, 2, 4, 8 ],
        #                l
        #     [ 10, 11, 12, 13 ],
        #
        #     [ 14, 20, 30, 40 ]
        #       r
        # ]

        # STEP 1: find relevant row - two pointers
        # STEP 2: find target within row if exists - binary search