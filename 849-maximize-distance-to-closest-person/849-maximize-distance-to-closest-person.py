class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        st, ed, mid, k = 0, 0, 0, 0
        
        for i in range(len(seats)):
            if seats[i] == 1:
                break
            st += 1
            
        for j in range(i+1, len(seats)):
            if seats[j] == 1:
                k += 1
                mid = max(mid, k)
                k = 0
            else:
                k += 1
        ed = k
        
        return max(max(st, mid//2), ed)
            