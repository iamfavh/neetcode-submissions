"""  Description
    We have an array of numbers. We need to find the longest consecutive
    sequence amongst the numbers.
"""
""" Requirements
    Time of O(n), n is the number of elements.
    Return the size of the largest consecutive sequence.
"""
""" Approach
    Identify the start of each sequence such that an element num - 1 does not exist
    in the given array of numbers. Once identified, we start counting the numbers
    consecutively greater to element num until the number doesn't exist in the set of numbers.
"""
""" Code / Pseudocode
    Create a set to store all elements num.
    Store all numbers in array in the set to eliminate duplicates.
    Create a variable to store the longest sequence
    Traverse the numbers in the set
        if the element is the start of a sequence
            Create a variable to track the length of the sequence
            increment length by 1
            Count forward until the next elemenet is not part of the set
                increment length by 1
            update the longest sequence
    return longest_sequence_size
"""
""" Efficiency
    Time: O(n)
    Space Complexity: O(n)
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        num_set = set(nums)

        longest = 0

        for num in num_set:
            if num - 1 not in num_set:
                length = 1
                while (num + length) in num_set:
                    length += 1
                longest = max(length, longest)
            
        return longest










