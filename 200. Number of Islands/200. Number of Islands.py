"""
200. Number of Islands (https://leetcode.com/problems/number-of-islands/description/)

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.

"""


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # empty grid
        if not grid or not grid[0]:
            return 0

        m = len(grid)
        n = len(grid[0])
        count = 0
        
        # utility to sink an entire island
        def dfs(i, j):
            # base case - check if we're out of bound or in water
            # if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
            if m <= i < 0 or n <= j < 0 or grid[i][j] == '0':
                return # stop recursion

            # mark current cell as visited by sinking it
            grid[i][j] = '0'

            # recursively explore all 4 directions
            dfs(i+1, j) # down
            dfs(i-1, j) # up
            dfs(i, j+1) # left
            dfs(i, j-1) # right

        # main loop - scan every cell in the grid
        for i in range(m):
            for j in range(n):
                # if we find a land that hasn't been visited
                if grid[i][j] == '1':
                    count += 1 # found a new island
                    dfs(i, j) # sink the entire island
        
        return count

            
