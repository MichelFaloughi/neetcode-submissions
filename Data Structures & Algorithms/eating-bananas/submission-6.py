class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # contraint: h >= len(piles), can i assume ? - yes

        # init best_k = max(piles) 

        # binary search, where condition is if candidate clears piles
        # keep updating best_k, while l < r or <= 

        best_k = max(piles)
        l, r = 1, best_k

        while l <= r: # TODO: check <=

            mid = (l + r) // 2

            # find the number of hours it takes for koko to clear piles at a rate of mid
            curr_h = sum( [ math.ceil(pile / mid) for pile in piles ] ) 

            if curr_h <= h: # TODO: check <= 
                best_k = mid
                r = mid - 1
            else:
                l = mid + 1
        
        return best_k
            
    
    # [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ]
    #  



        
        