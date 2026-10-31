class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        low = 0
        high = len(nums)

        while low < high: 
            
            m = low + (high - low) // 2

            if target == nums[m]:
                return m
    
            elif target < nums[m]:
                high = m
    
            else:
                # target is larget
                low = m + 1

        return -1
        

        
        

            
