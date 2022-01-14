class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if s == '' or s == '+' or s == '-':
            return int('0')
        res = ''
        for i, ch in enumerate(s):
            if i == 0:
                if ch == '+' or ch == '-' or ch.isdigit():
                    res += ch
                else:
                    return int('0')
            else:
                if i == 1 and (ch == '+' or ch == '-'):
                    return int('0')
                else:
                    if ch != '.':
                        if ch.isdigit():
                            res += ch
                        else:
                            break
                    else:
                        break
        print(res)
        if res == '+' or res == '-':
            return int('0')
        if int(res) <= int("-2147483648"):
            res = int("-2147483648")
        if int("2147483648") <= int(res):
            res = int("2147483648") - 1
        return int(res)
