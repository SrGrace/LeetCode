class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        cnt, minEnd = 0, float('inf')
        points.sort(key=lambda x: x[0])
        print(points)
        for p in points:
            if p[0] > minEnd:
                cnt += 1
                minEnd = p[1]
            else:
                minEnd = min(minEnd, p[1])
                
        return cnt + int(len(points) != 0)
    
    
    