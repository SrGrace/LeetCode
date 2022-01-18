class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        cnt = 0
        for i in range(0, len(flowerbed)):
            if flowerbed[i] == 0:
                if (i == 0 or flowerbed[i-1] == 0) and (
                    i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                    cnt += 1
                    flowerbed[i] = 1
        return cnt >= n