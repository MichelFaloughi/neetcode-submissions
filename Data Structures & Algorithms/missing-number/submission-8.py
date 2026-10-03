class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = len(nums)
        
        # total = sum([i for i in range(n + 1)])
        total = int(( n * (n + 1) ) / 2)

        # 0 1   2   3 ...   n-2 n-1 n
        # n n-1 n-2 n-3 ... 2   1   0
        #
        # n*(n+1)/2




        return total - sum(nums)

        
        

        





        
        