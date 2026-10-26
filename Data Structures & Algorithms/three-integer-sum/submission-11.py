# Translation
"""
We need to find all 3-number combinations that sum up to 0.
"""
# Requirements
"""
No duplicates.
We must output a list containing each combination.
If none are found then we output an empty list.
"""
# Approach
"""
Sort the array in ascending order. We can afford O(n^2) since our
input is at most 3000 elements.
We'll use the equation x + y + z = 0 and solve for x which yields,
    x = -(y + z).
Knowing our array is sorted in ascending order, 
we'll use the following pointers:
    x to the target, 
    y to the smaller values,
    z to the larger values.
That being said, if the value at x is -9,
    then y will point to 4 and z to 5.
That's 1 benefit of sorting, another benefit is that we can avoid
duplicates by skipping values at x which found a triplet. So,
the previous value -9 would be skipped until a different value shows up.
i.e. 
    input = [-9,0,0,0,1,2,4,5]

    x will start at index = 0, target is -9
    y will start at index = x + 1, value is 0
    z will start at index len(nums) -1, value is 5

    we plug the values into x = -(y + z), which yields -5.
    since the value is greater than the target, we increment y.
    we do that computation until we find that the value 4 solves our equation.
    -9 = -(4 + 5), which in turn is the triplet that sums up to 0.
"""
# Pseudocode
"""
sort(nums)

x = 0
y = x + 1
z = len(nums) - 1

res = []

# iterate the array until when x reaches the 2nd to last element in the array
    # let the target equal the value at x
    # if the equation equals 0, add to the list
        # increment x until a different value is found
        # let y be x + 1
        # let z be len(nums) - 1
    # if the equation yields a value greater than the target
        # increment y
    # else decrement z
# return the result
"""
# efficiency
"""
Sorting yields O(n^2)
Finding the target yields O(n)
O(n^2) at worst case
"""

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)

        i = 0
        res = []
        target = 0

        while i <= len(nums) - 3:
            
            j = i + 1
            k = len(nums) - 1

            while j < k:
                total = nums[i] + nums[j] + nums[k]
                
                if total < target:
                    j += 1
                elif total > target:
                    k -= 1
                else:
                    res.append([nums[i], nums[j], nums[k]])

                    old_j = j
                    while j != k and nums[old_j] == nums[j]:
                        j += 1
                        
                    old_k = k
                    while k != j and nums[old_k] == nums[k]:
                        k -= 1
            
            old_i = i
            while i <= len(nums) - 3 and nums[old_i] == nums[i]:
                i += 1

        return res








