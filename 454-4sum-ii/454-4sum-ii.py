class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        ij = collections.Counter(i+j for i in nums1 for j in nums2)
        # print(ij)
        return sum(ij[0-(k+l)] for k in nums3 for l in nums4) # O(n^2), O(n^2)
        
        
