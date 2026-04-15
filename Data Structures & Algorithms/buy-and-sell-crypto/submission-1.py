class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        l, r = 0, 0
        
        while r < len(prices):
            profit = prices[r] - prices[l]
            print(profit)
            if profit > 0:
                max_profit = max(max_profit, profit)
            else:
                l = r
            r += 1
        print('l', l, 'r', r)
        return max_profit
    
    # [7, 1, 5, 3, 6, 4]
    #     l   
    #              r                
        

# learnings:
# - The idea is, one pass of the array ( O(n) time ), O(1) space

