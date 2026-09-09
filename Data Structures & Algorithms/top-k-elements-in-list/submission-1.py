class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        """ Problem
            We have an unsorted array of integers. I want to keep track of the
            k most frequent elements within the array.
        """
        """ Requirements
            The output must contain the k most frequent elements [in any order].
            process at most 10,000 numbers.
        """
        """ Approach
            we can use a counter array with the size of the elements stored in nums.
            by storing their frequency in a map, we can then fill the counter array
            with the number at the count/index of each element.
            We get the top k by traversing the counter array in reverse order
            since the counter array will be in non-descending order.
        """
        
        freq_map = {}
        # store the count of the numbers
        for num in nums:
            if num not in freq_map:
                freq_map[num] = 1
            else:
                freq_map[num] += 1
        
        counter = []
        for i in range(len(nums)+1):
            counter.append([])
        
        for num, count in freq_map.items():
            counter[count].append(num)
        
        res = []
        for i in range(len(counter)-1, 0, -1):
            for num in counter[i]:
                res.append(num)
                if len(res) == k:
                    return res

        
        return res
