class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hsh = dict()
        for i in range(len(nums)):
            if target - nums[i] in hsh:
                return [i, hsh[target - nums[i]]]
            else:
                hsh[nums[i]] = i
        return -1 # O(n), O(n)
