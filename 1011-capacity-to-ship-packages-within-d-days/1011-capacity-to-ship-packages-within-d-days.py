class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def min_ship_req(max_load_allowed):
            cur_load, ship_req = 0, 0
            for w in weights:
                cur_load += w
                if cur_load > max_load_allowed:
                    cur_load = w
                    ship_req += 1
                    
            return ship_req + 1
        
        l, r = max(weights), sum(weights)
        while(l < r):
            max_load_allowed = l + (r-l)//2
            if min_ship_req(max_load_allowed) <= days:
                r = max_load_allowed
            else:
                l = max_load_allowed + 1
        
        # O(nlog(sum(weights))), O(1)
        return l
                
        