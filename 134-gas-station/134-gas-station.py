class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        tot, subSum, st = 0, float('inf'), 0
        for i in range(n):
            if tot < subSum:
                subSum = tot
                st = i
            tot += gas[i] - cost[i]
        
        return -1 if tot < 0 else st
    
    
    
    