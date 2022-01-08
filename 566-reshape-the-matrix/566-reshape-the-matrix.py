import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        mat = np.array(mat)
        if mat.shape[0]*mat.shape[1] != r*c:
            return mat
        return np.reshape(mat, (r, c))
                          