# Translation
""" 
We are given a list of numbers in ascending order. We need to find
the positions of two numbers which add up to a given target.
"""
# Requirements
"""
Output must be a list of two integers representing the 1-indexed 
position of the two numbers in ascending order.
So, Position 1 must be less than Position 2.
"""
# Approach
""" 
We know that num1 + num2 = target. 
We also know that the numbers are ascending order.
We can use two pointers; one at the start (left) and another at the end (right).
The left pointer is the smallest and right pointer is the largest.
The sum of these two will depict which pointer to move next to increase or decrease our sum.
"""
# Pseudocode
"""
l = 0
r = end of list of integers 

traverse the list until the left crosses the right index
    sum = nums[l] + nums[r]
    if sum == target
        return [l+1,r+1] # 1-indexed
    
    if sum < target:    
        l += 1          # add more by shifting the left ptr
    else:               
        r -= 1          # subtract by shifting the right ptr

return [-1,-1] # error, not found
"""

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        l = 0
        r = len(numbers) - 1

        while l < r:

            total = numbers[l] + numbers[r]
            if total == target:
                return [l+1,r+1] # 1-indexed
            
            # shift left or right
            if total < target:
                l += 1
            else:
                r -= 1
                
        return [-1, -1]








        