class Solution:
    def bitwiseComplement(self, n: int) -> int:
        # def bin2dec(binary): 
        #     decimal = 0
        #     for digit in binary:
        #         decimal = decimal*2 + int(digit)
        #     return decimal
        #
        # bin_len = len(bin(n)[2:]) # O(logn)
        # # print(bin_len, '1'*bin_len, bin2dec('1'*bin_len))
        # # O(logn*len(bin_len))
        # comp = bin2dec('1'*bin_len) - n  # comp = dec(full_bin - bin)
        # return comp
        
        # O(logn)
        p = 2  # smallest power of 2 larger than n
        while p <= n:
            p *= 2
        return p - 1 - n  # comp = p-1-n
    
        
