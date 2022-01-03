class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        cnt = 0
        # O(n^2), O(1): TLE
        # for i in range(len(time)):
        #     for j in range(i+1, len(time)):
        #         if (time[i]+time[j])%60 == 0:
        #             cnt += 1
        
        # O(n), O(60): Success
        hsh = [0]*60
        for x in time:
            t = x%60
            y = (60-t)%60
            cnt += hsh[y]
            hsh[t] += 1
        return cnt