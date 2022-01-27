class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        n = len(nums)
        max_xor = 0
        # for i in range(n):
        #     for j in range(i, n):
        #         max_xor = max(max_xor, nums[i]^nums[j])
        # return max_xor
        
        mask = 0
        st = set()
        for i in range(30, -1, -1):
            # set the i'th bit in mask like 100000, 110000, 111000..
            mask |= (1 << i)
            newMaxx = max_xor | (1 << i)
            
            for i in range(n): 
                # Just keep the prefix till i'th bit neglecting all the bit's after i'th bit
                st.add(nums[i] & mask)
            
            for prefix in st:
             
                # find two pair in set such that a^b = newMaxx
                # which is the highest possible bit can be obtained
                if (newMaxx ^ prefix) in st:
                    max_xor = newMaxx
                    break

            # clear the set for next iteration
            st.clear()
        return max_xor
    