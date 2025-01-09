class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        lis = [1]*(n+1)

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], 1+lis[j])
        
        # ans = 0
        # for i in range(n):
        #     ans = max(ans, lis[i])
        
        return max(lis) # ans #O(n^2)
        
