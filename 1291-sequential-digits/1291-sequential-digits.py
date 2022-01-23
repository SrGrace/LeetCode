class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        res = list()
        for digit in range(1, 9):
            num = nxt = digit
            while(num <= high and nxt < 10):
                if num >= low:
                    res.append(num)
                nxt += 1
                num = num*10 + nxt
                
        return sorted(res)
    