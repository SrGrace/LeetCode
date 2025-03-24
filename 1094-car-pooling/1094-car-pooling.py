from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        mp = defaultdict(int)
        for t in trips:
            mp[t[1]] += t[0] # passenger get on
            mp[t[2]] -= t[0] # passenger get off
        
        print(mp)
        # sort by location
        mp = sorted(mp.items(), key=lambda x: x[0])
        print(mp)
            
        for k, v in mp:
            capacity -= v
            if capacity < 0:
                return False
        return True  # O(nlogn), O(n)
    
