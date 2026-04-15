class Solution(object):
    def Dynamic(self,nums,i,L):
        if i < 0:
            return 0 
        elif L[i]!=-1:
            return L[i]
        else:
            L[i]=max(nums[i]+ self.Dynamic(nums,i-2,L),self.Dynamic(nums,i-1,L))
            return L[i]
        
        
    def rob(self, nums):
        i=len(nums)-1
        L=[-1 for m in range(len(nums))]
        return self.Dynamic(nums,i,L)