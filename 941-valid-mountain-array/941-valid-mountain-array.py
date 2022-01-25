class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n <= 2:
            return False
        
        flg = arr[1] > arr[0]
        if not flg:
            return False
        
        for i in range(1, n):
            if arr[i] == arr[i-1]:  # flat
                return False
            if flg:
                if arr[i] < arr[i-1]:  # peak
                    flg = False
            else:
                if arr[i] > arr[i-1]:
                    return False
                
        return not flg
    