class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        hsh = dict()
        for n in nums:
            if n in hsh:
                hsh[n] += 1
            else:
                hsh[n] = 1
        
        # hsh = collections.Counter(nums)
        
        cnt = 0
        if k > 0:
            cnt = sum([i+k in hsh for i in hsh])
        else:
            cnt = sum([hsh[i] > 1 for i in hsh]) # looking for pair of equal nums
            
        return cnt
        
                
        