class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # O(n), O(n)
        cnt = sm = 0
        hsh = defaultdict(int)
        hsh[0] = 1
        for n in nums:
            sm += n
            cnt += hsh[sm-k]
            hsh[sm] += 1
        return cnt
    
    