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
    


# 2nd approach
class Solution:
    def carPooling(trips, capacity):
        max_location = 1001  # Assuming locations are between 0 and 1000
        changes = [0] * (max_location + 1)
    
        for numPassengers, from_loc, to_loc in trips:
            changes[from_loc] += numPassengers # passenger get on
            changes[to_loc] -= numPassengers  # passenger get off
    
        current_passengers = 0
        for change in changes:
            current_passengers += change
            if current_passengers > capacity:
                return False
    
        return True  # O(n+m), O(n)

# Example usage:
trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
print(carPooling(trips, capacity))  # Output: False
