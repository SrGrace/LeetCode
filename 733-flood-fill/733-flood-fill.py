class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # dfs - O(n), O(n)
        color = image[sr][sc]
        if color == newColor:
            return image
        
        m, n = len(image), len(image[0])
        def dfs(r, c):
            if 0 <= r < m and 0 <= c < n and image[r][c] == color:
                image[r][c] = newColor
                dfs(r-1, c); dfs(r+1, c)
                dfs(r, c-1); dfs(r, c+1)
        dfs(sr, sc)
        return image
    