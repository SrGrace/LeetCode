class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Line 1: Create a dictionary to store the most recent index of each character
        hsh = dict()
        
        # Line 2: Initialize variables:
        # res = maximum length found so far
        # last_match = the index AFTER the last duplicate character found
        # (starts at -1 so first character calculation works correctly)
        res, last_match = 0, -1
        
        # Line 3: Iterate through each character in the string with its index
        for i, ch in enumerate(s):
            
            # Line 4: Check if current character was seen before AND
            # the last occurrence is within our current window (after last_match)
            if ch in hsh and last_match < hsh[ch]:
                # Line 5: Update last_match to the position of the duplicate character
                # This moves the start of our window to after the duplicate
                last_match = hsh[ch]
            
            # Line 6: Calculate current substring length and update maximum
            # i - last_match = length from (last_match + 1) to i
            res = max(res, i - last_match)
            
            # Line 7: Update the hash with current character's position
            hsh[ch] = i
        
        # Line 8: Return the maximum length found
        return res # O(n), O(n)
