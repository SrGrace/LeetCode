class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hsh = dict()
        for n in nums1:
            if n in hsh:
                hsh[n] += 1
            else:
                hsh[n] = 1
        res = list()
        for n in nums2:
            if n in hsh and hsh[n] > 0:
                res.append(n)
                hsh[n] -= 1
        return res # O(n), O(n)
    
