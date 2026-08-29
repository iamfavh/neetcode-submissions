class Solution:
    
    h_map = {};

    def hasDuplicate(self, nums: List[int]) -> bool:
        
        
        """ Problem
            An array that may or may not contain a duplicate.
            Find whether it contains a duplicate element.
        """
        """ Requirements
            Do:
                accept an empty array
            Don't:
                accept an array of size < 10^5
                accept a number > 10^9 or < -10^9
            The acceptable criteria is to return whether an array of integers
                contains a duplicate or not.
        """
        """ Approach
            We can use O(n) space to store store all of the integers.
            While iterating the list;
            We'll store the integers in a set.
            Using the set, we can identify if a key exists in O(1) time.
            return true if it's a duplicate.
            return false if we exhaust the list
        """
        """ Pseudocode

            num_set = set()

            for num in nums

                if num_set.contains(num)
                    return true
                else
                    num_set.add(num)
            
            return false # exhausted all elements
        """
        """ Efficiency
            We can expect to use:
                O(n) space
                O(n) time
        """

        num_set = set()

        for num in nums:
            if num not in num_set:
                num_set.add(num)
            else:
                return True
        
        return False


        










