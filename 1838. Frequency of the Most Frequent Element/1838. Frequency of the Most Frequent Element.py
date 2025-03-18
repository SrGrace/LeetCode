class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        # Sort the array to group similar elements together
        # Time Complexity: O(N log N) for sorting
        nums.sort()

        # Initialize variables:
        # i: left pointer of the sliding window
        # N: length of the array
        # ans: to store the maximum frequency found
        # sum_: to store the sum of elements in the current window
        i, N, ans, sum_ = 0, len(nums), 1, 0

        # Iterate over the array using the right pointer j
        # Time Complexity: O(N) for the sliding window traversal
        for j in range(N):
            # Add the current element to the sum of the window
            sum_ += nums[j]

            # While the current window cannot be converted to all nums[j] with <= k operations:
            # Calculate the required operations: (window size) * nums[j] - sum_
            # If it exceeds k, shrink the window from the left
            while (j - i + 1) * nums[j] - sum_ > k:
                sum_ -= nums[i]
                i += 1

            # Update the maximum frequency found so far
            ans = max(ans, j - i + 1)

        # Return the maximum frequency
        return ans
    
