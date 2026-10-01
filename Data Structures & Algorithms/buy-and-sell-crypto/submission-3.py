class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # [10, 1, 5, 6, 7, 0, 3, 20]
        #  b                        s

        # maybe init maxP = 0 ? b = 0, s = 1
        # while s < len(prices):
        #   if green:
        #       update maxP = max(maxP, p)
        #.  else:
        #.      increment b to s and s to s + 1
        # return maxP
        
        maxP, b, s = 0, 0, 1
        while s < len(prices):
            PnL = prices[s] - prices[b]
            if PnL >= 0: # TODO: check > or >=
                maxP = max(maxP, PnL)
                s += 1
            else:
                b, s = s, s + 1
        return maxP