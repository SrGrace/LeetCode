class Solution:
    def bitwiseComplement(self, n: int) -> int:
        def bin2dec(binary):
            decimal = 0
            for digit in binary:
                decimal = decimal*2 + int(digit)
            return decimal
        
        bin_len = len(bin(n)[2:])
        # print(bin_len, '1'*bin_len, bin2dec('1'*bin_len))
        return bin2dec('1'*bin_len) - n
