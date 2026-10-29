# Translate
"""
We are given an array of heights which represent elevation on map.
We must analyze the heights and find all the water that can be trapped
in the map.
"""
# Requirements
"""
Output the value as an integer.
There's at most 20,000 heights so we can afford O(n^2) or better.
"""
# Approach
"""
We'll use two pointers to track the water through the list of heights.
We'll need to find out how much water is at the following moments:
    held in a single space, with lesser elevations but a common min_elevation
    held between a large space, with varying elevations at the bottom but a min_elevation
    or when there is no water at all
"""
# Pseudocode
"""    
        

"""


class Solution:
    def trap(self, height: List[int]) -> int:
        
       
        left, right = 0, len(height) - 1
        left_max = right_max = 0
        res = 0

        while left < right:
            if height[left] < height[right]:
                # right side guarantees a taller wall, so left_max bounds the water
                if height[left] >= left_max:
                    left_max = height[left]      # new wall, no water here
                else:
                    res += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res
