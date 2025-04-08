class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far, cur_max = nums[0], nums[0]
        for i in range(1, len(nums)):
            cur_max = max(nums[i], cur_max+nums[i])
            max_so_far = max(max_so_far, cur_max)
        return max_so_far # O(n), O(1)
