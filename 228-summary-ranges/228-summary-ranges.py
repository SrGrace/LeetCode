class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        
        res, i, st = list(), 0, 0
        while(i < len(nums)-1):
            if nums[i]+1 != nums[i+1]:
                res.append(self.printRange(nums[st], nums[i]))
                st = i+1
            i += 1
            
        res.append(self.printRange(nums[st], nums[i]))
        return res

    def printRange(self, l, r):
        if l == r:
            return str(l)
        else:
            return str(l) + "->" + str(r)
                
                    