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




class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)
        lis = [0]*(n+1)

        ans = 0
        for x in nums:
            i, j = 0, ans
            while i != j:
                mid = i + (j-i)//2
                if lis[mid] < x:
                    i = mid + 1
                else:
                    j = mid
            lis[i] = x
            ans = max(ans, i+1)
        return ans #O(nlogn)

        
