class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dp, res = 0, 0
        for i in range(2, len(nums)):
            if nums[i-1] - nums[i-2] == nums[i] - nums[i-1]:
                dp += 1
            else:
                dp = 0
            res += dp
                
        return res
    
    