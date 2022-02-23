class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = pos = 0
        for lett in reversed(columnTitle):
            dig = ord(lett) - 64
            res += dig * 26 ** pos
            pos += 1
            
        return res
    
    