class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # maybe init maxP = 0 ?

        # [10, 1, 5, 6, 7, 1]
        #      l  r
        maxP, l = 0, 0

        while l < len(prices) - 1:
            r = l + 1
            while r <= len(prices) - 1:
                maxP = max(
                    prices[r] - prices[l],
                    maxP
                )
                r += 1
            l += 1
        return maxP
        