# import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        # mat = np.array(mat)
        # if mat.shape[0]*mat.shape[1] != r*c:
        #     return mat
        # return np.reshape(mat, (r, c))
        
        m, n = len(mat), len(mat[0])
        if m*n != r*c:
            return mat
        
        reshaped = [[0]*c for _ in range(r)]
        for i in range(r*c):
            reshaped[i//c][i%c] = mat[i//n][i%n]
        return reshaped
                          