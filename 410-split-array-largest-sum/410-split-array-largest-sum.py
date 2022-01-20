class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def min_subarrays_required(max_sum_allowed):
            cur_sum, split_req = 0, 0
            for n in nums:
                # if cur_sum + n <= max_sum_allowed:
                cur_sum += n
                # else:
                if cur_sum > max_sum_allowed:
                    cur_sum = n
                    split_req += 1
                    if split_req + 1 > m:
                        return 0
                    
            return 1  # split_req + 1
        
        l, r = max(nums), sum(nums)
        while(l < r):
            max_sum_allowed = l + (r-l)//2
            # if min_subarrays_required(max_sum_allowed) <= m:
            #     r = max_sum_allowed - 1
            #     min_largest_split_sum = max_sum_allowed
            if min_subarrays_required(max_sum_allowed):
                r = max_sum_allowed
                
            else:
                l = max_sum_allowed + 1
                
        # O(nlog(sum(nums))), O(1)
        return l  # min_largest_split_sum
    
    