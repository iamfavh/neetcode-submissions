# Translate
"""
    We need to go over each element E_k, and replace it with the product 
    of all elements E_i where i >= 1, i <= total elements, and i != k.
"""
# Requirements
"""
    The function must accept at least 2 elements.
    Each number may consist of negative and non-negative integers.
    Each product is guaranteed a 32-bit integer.
    Do not use the division operation.
    Solve in O(n)
"""
# Approach
"""
    We'll use a rule of multiplication, the associative property lets us
    multiply all elements from the left to right to keep the total associative value at
    that time (same from right to left).
    We store these values in two arrays, left and right,
    respectively.
    We'll then compute Left_k-1 * Right_k+1 where k >= 0 and k < length(elements)
"""
# Code / Pseudocode
"""
    # multiply the values from left to right
    for each number n in nums from 0 to N-1
        left[i] *= n

    # multiply the values from right to left
    for each number n in nums from N-1 to i = 0
        right[i] *= n
    
    # compute the value at the current element
    for each number n in nums from 0 to N-1
        if i == 0:
            nums[i] = right[i+1]
        elif i == len(nums)-1:
            nums[i] = left[i-1]
        else:
            nums[i] = left[i-1] * right[i+1]
"""
# Efficiency
"""
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        
        l_prod = []
        for n in nums:
            l_prod.append(n)

        for i in range(1, len(nums)):
            
            l_prod[i] = l_prod[i-1] * nums[i]
        
        r_prod = []
        for n in nums:
            r_prod.append(n)

        for i in range(len(nums)-2, -1, -1):
            r_prod[i] = nums[i] * r_prod[i+1]

        res = nums
        
        for i in range(len(nums)):
            if i == 0:
                res[i] = r_prod[1]
            elif i == len(nums)-1:
                res[i] = l_prod[i-1]
            else:
                res[i] = l_prod[i-1] * r_prod[i+1]
        

        return res












        