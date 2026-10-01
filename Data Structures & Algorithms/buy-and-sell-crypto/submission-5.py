class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxP, b, s = 0, 0, 1

        while s < len(prices):
            pnl = prices[s] - prices[b]
            if pnl > 0:
                maxP = max(maxP, pnl)
                s += 1
            else:
                b, s = s, s + 1
        return maxP

        # [10, 1, 5, 6, 7, 1, 0, 20]
        #                     b     s


