"""
4. Median of Two Sorted Arrays
Solved
Hard
Topics
premium lock icon
Companies
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # ensure nums1 is the smaller array for O(log(min(m,n))), O(1) solution
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # initialization
        m, n = len(nums1), len(nums2)
        total = m+n
        half = total // 2 
        left, right = 0, m

        # binary search loop
        while(left <= right):
            i = (left+right)//2 # elements from nums1 in left half
            j = half - i # elements from nums2 in left half

            # handling boundaries (edge cases)
            nums1_left_max = float('-inf') if i == 0 else nums1[i-1]
            nums1_right_min = float('inf') if i == m else nums1[i]
            nums2_left_max = float('-inf') if j == 0 else nums2[j-1]
            nums2_right_min = float('inf') if j == n else nums2[j]

            # perfect partition check
            if nums1_left_max <= nums2_right_min and nums2_left_max <= nums1_right_min:
                # median calculation
                if total % 2 == 1:
                    return min(nums1_right_min, nums2_right_min)
                else:
                    return (max(nums1_left_max, nums2_left_max) + min(nums1_right_min, nums2_right_min))/2
            # If nums1's left is too large, reduce elements from nums1. 
            elif nums1_left_max > nums2_right_min:
                right = i - 1
            # Otherwise, increase them.
            else:
                left = i + 1

          
