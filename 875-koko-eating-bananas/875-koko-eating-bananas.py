class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        # O(nlogm), O(1)
        while(l < r):
            mid = l + (r-l)//2
            hr_spent = 0
            for p in piles:
                hr_spent += math.ceil(p/mid)
            if hr_spent <= h:
                r = mid
            else:
                l = mid + 1
                
        return r
    
    
