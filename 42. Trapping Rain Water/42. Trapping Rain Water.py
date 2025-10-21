"""
42. Trapping Rain Water (https://leetcode.com/problems/trapping-rain-water/description/)

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

 
Example 1:


Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
 

Constraints:

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

"""

class Solution:
    def trap(self, height: List[int]) -> int:
        # Line 1-2: Handle edge case - empty array
        if not height:
            return 0
        
        # Line 3-4: Initialize two pointers at both ends of the array
        left, right = 0, len(height) - 1
        
        # Line 5: Track the maximum heights seen from left and right
        left_max, right_max = 0, 0
        
        # Line 6: Variable to accumulate total trapped water
        water = 0
        
        # Line 7: Main loop - continue until pointers meet
        while left <= right:
            # Line 8: Decide which side to process
            # We process the side with smaller current height
            if height[left] <= height[right]:
                # Line 9-10: If current height is greater than left_max,
                # update left_max (no water can be trapped here)
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    # Line 11-12: Water can be trapped here!
                    # The water level is determined by left_max (since we know
                    # there's a taller wall on the right from our condition)
                    water += left_max - height[left]
                
                # Line 13: Move left pointer forward
                left += 1
            
            else:
                # Line 15-19: Same logic but for right side
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    # Line 20-21: Water trapped on right side
                    # Water level determined by right_max (since we know
                    # there's a taller wall on the left from our condition)
                    water += right_max - height[right]
                
                # Line 22: Move right pointer backward
                right -= 1
        
        # Line 24: Return total trapped water
        return water
      
