class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree = [0]*(n+1)
        for x, y in trust:
            degree[x] -= 1
            degree[y] += 1
        print(degree)
        for i in range(1, n+1):
            if degree[i] == n-1:
                return i
        return -1 # O(n), O(n)
            
