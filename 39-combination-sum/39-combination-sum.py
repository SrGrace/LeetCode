class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        candidates.sort()
        res = list()
        
        def dfs(idx, target, path):
            if target < 0:
                return True
            
            if target == 0:
                res.append(path)
                return False
            
            for i in range(idx, n):
                if dfs(i, target-candidates[i], path + [candidates[i]]):
                    break
                    
        dfs(0, target, [])
        return res
            