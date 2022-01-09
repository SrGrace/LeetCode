class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def bin_search(a, t):
        #     l, r = 0, len(a) - 1
        #     while(l < r):
        #         mid = l + (r-l)//2
        #         if a[mid] == t:
        #             return 1
        #         elif a[mid] < t:
        #             l = mid + 1
        #         else:
        #             r = mid - 1
        #     return 0
        
        # for i in range(len(matrix)):
        #     if bin_search(matrix[i], target):
        #         return 1
        # return 0
        
        m, n = len(matrix), len(matrix[0])
        i, j = m-1, 0
        while(i >= 0 and j < n):
            if matrix[i][j] == target:
                return 1
            elif matrix[i][j] > target:
                i -= 1
            else:
                j += 1
                
        return 0
    