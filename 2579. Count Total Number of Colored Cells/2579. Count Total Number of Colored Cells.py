class Solution:
    def coloredCells(self, n: int) -> int:
        # return 1 + n * (n-1) * 2 ## O(1)
        result = 1
        for i in range(n):
            result += 4*i
        return result ## O(n)
