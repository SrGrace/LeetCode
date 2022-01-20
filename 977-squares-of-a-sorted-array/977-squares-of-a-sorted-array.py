class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums)-1
        res = [0]*len(nums)
        while(l <= r):
            ll, rr = abs(nums[l]), abs(nums[r])
            if ll > rr:
                res[r-l] = ll*ll
                l += 1
            else:
                res[r-l] = rr*rr
                r -= 1
                
        return res
    
    