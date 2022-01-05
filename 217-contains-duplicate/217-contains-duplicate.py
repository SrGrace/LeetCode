class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hsh = dict()
        for n in nums:
            if n in hsh:
                hsh[n] += 1
            else:
                hsh[n] = 1
        for k, v in hsh.items():
            if v > 1:
                return 1
        return 0