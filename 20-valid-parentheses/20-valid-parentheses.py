class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 == 1: 
            return False
        
        stack = ["default"]
        mp = {
            ']': '[',
            '}': '{',
            ')': '('
        }
        for ch in s:
            # print('for: {}'.format(ch))
            if ch in mp:
                # print('if: {}'.format(stack.pop(), mp[ch]))
                if stack.pop() != mp[ch]:
                    return False
            else:
                # print('else: {}'.format(ch))
                stack.append(ch)
        return len(stack) == 1 # O(n), O(1)
    
    
