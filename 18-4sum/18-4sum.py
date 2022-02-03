class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # nums.sort()
        # hsh = dict()
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i]+nums[j] in hsh:
        #             hsh[nums[i]+nums[j]].append((i, j))
        #         else:
        #             hsh[nums[i]+nums[j]] = [(i, j)]
        #            
        # res = set()
        # for k in hsh:
        #     v = target-k
        #     if v in hsh:
        #         ab = hsh[k]
        #         cd = hsh[v]
        #         for (i, j) in ab:
        #             for (k, l) in cd:
        #                 if i != k and i != l and j != k and j != l:
        #                     tmp = [nums[i], nums[j], nums[k], nums[l]]
        #                     tmp.sort()
        #                     res.add(tuple(tmp))
        # return list(res)
        
        nums.sort()
        n = len(nums)
        ans = set()
        for i in range(n):
            for j in range(i+1, n):
                l, r = j + 1, n - 1
                remain = target - nums[i] - nums[j]
                while l < r:
                    if nums[l] + nums[r] == remain:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                        r -= 1
                    elif nums[l] + nums[r] > remain:
                        r -= 1
                    else:
                        l += 1
        return ans
        