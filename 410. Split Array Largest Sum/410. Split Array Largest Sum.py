class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        # Helper function to check if a given threshold is feasible
        # Time Complexity: O(N), where N is the length of nums
        def feasible(threshold):
            count, total = 1, 0  # Initialize subarray count and running total
            for num in nums:
                total += num  # Add the current number to the running total
                if total > threshold:  # If the running total exceeds the threshold
                    total = num  # Start a new subarray with the current number
                    count += 1  # Increment the subarray count
                    if count > k:  # If the number of subarrays exceeds k, the threshold is not feasible
                        return False
            return True  # The threshold is feasible

        # Initialize the search range:
        # left: the maximum element in nums (smallest possible threshold)
        # right: the sum of all elements in nums (largest possible threshold)
        left, right = max(nums), sum(nums)

        # Perform binary search to find the minimum feasible threshold
        # Time Complexity: O(log(S)), where S is the sum of nums
        while left < right:
            mid = left + (right - left) // 2  # Calculate the middle point
            if feasible(mid):  # If the threshold is feasible, try a smaller threshold
                right = mid
            else:  # If the threshold is not feasible, try a larger threshold
                left = mid + 1

        # Return the minimum feasible threshold
        return left # O(Nlog(S))

