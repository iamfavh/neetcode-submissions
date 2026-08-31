class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        """ Problem
            Find the 2 numbers that add up to the given target in a given array.
        """
        """ Requirements
            The 2 numbers must be unique elements.
            Assume there will always be only 1 solution.
            Return the indices in the order they were given from left to right.
        """
        """ Approach
            Store data in a key-value list, where each key
            represents a number in the array and its value is its respective indice.
            Then, iterate the array again to find the missing number; the difference 
            between the target and the current number.
                other_num =  target - current_num
                other_num is in nums_map
            After inevitably finding the missing number, we return the indices,
            in non-decreasing order.
        """
        """ Pseudocode

            key_values = init()

            for i = 0; i ... nums.length-1
                key_values[nums[i]] = i

            for i = 0: i ... nums.length-1
                diff = target - nums[i]
                if diff in key_values
                    k = max(i, key_values[diff])
                    return [j, k]
                else:
                    continue
        """
        """ Efficiency
            We traverse the array twice.
            We store all the number in a list of the size of the array.
            Time: O(n)
            Space: O(n)
        """

        key_values = {}

        for i in range(len(nums)):
            key_values[nums[i]] = i

        for i in range(len(nums)):

            diff = target - nums[i]
            
            if diff in key_values and key_values[diff] != i:
                
                j = min(i, key_values[diff])
                k = max(i, key_values[diff])
                return [j, k]

        return [-999,999] # error



















