class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cand, cnt, n = 0, 1, len(nums)
        for i in range(1, n):
            if nums[i] == nums[cand]:
                cnt += 1
            else:
                cnt -= 1
            if cnt == 0:
                cand = i
                cnt = 1
        k = 0
        for i in range(n):
            if nums[i] == nums[cand]:
                k += 1
                
        if k > n // 2:
            return nums[cand]
        else:
            return -1
        