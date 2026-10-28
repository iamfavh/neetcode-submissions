# Translate
"""
We are given an array of heights and need to find the largest 
area between those heights.
"""
# Requirements
"""
Output the max area in integer.
The largest input could be 100,000 heights so we need something
better than O(n^2).
"""
# Approach
"""
To compute the areas: 
    we use two pointers to keep calculating the area between the left
    and right extremes of the list until a pointer crosses the other.
    That puts us at O(n) because we need to explore the whole list.
To keep track of the best area:
    We'll use a greedy approach where we move the pointers based on
    whether the area gets larger or not.
    The area will get larger as the minimum height between the two pointers increases.
"""
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largestArea = 0

        l = 0
        r = len(heights) - 1
        
        while l < r:
            
            area = self.computeArea(r-l, min(heights[l],heights[r]))

            largestArea = max(largestArea, area)
            
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1

        return largestArea

    def computeArea(self, width, height):
        return width * height















