class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def min_ship_req(max_load_allowed):
            cur_load, ship_req = 0, 0
            for w in weights:
                cur_load += w
                if cur_load > max_load_allowed:
                    cur_load = w
                    ship_req += 1
                    if ship_req + 1 > days:
                        return 0
                    
            return 1  # ship_req + 1
        
        l, r = max(weights), sum(weights)
        while(l < r):
            max_load_allowed = l + (r-l)//2
=
            if min_ship_req(max_load_allowed):
                r = max_load_allowed
            else:
                l = max_load_allowed + 1
        
        # O(nlog(sum(weights)−max(weights))), O(1)
        return l

    ## 2nd method
    def shipWithinDays(weights, days):
        left = max(weights)
        right = sum(weights)
        
        def can_ship(capacity):
            days_needed = 1
            current_weight = 0
            for weight in weights:
                if current_weight + weight > capacity:
                    days_needed += 1
                    current_weight = 0
                current_weight += weight
            return days_needed <= days
        
        while left < right:
            mid = left + (right - left) // 2
            if can_ship(mid):
                right = mid
            else:
                left = mid + 1
        return left  # O(nlog(sum(weights)−max(weights))), O(1)
        
