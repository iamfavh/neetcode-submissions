class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        """ Problem
            We have an array of words, and we want to group them by anagrams.
            
            The output should demonstrate the groups, and order doesn't matter.
        """
        """ Requirements
            - strings must meet between 0 to 100 characters
            - the array must be between 1 and 10000 words
            - strings are made up of lowercase English letters
        """
        """ Approach

            1. create a key for every anagram, so we can use it to
            identify which group it belongs to.
                - create a function that returns the key, identifying the anagram
                - using the key, we can either create a new group or add it to an
                    existing group
                - output the groups
        """
        """ Pseudocode

            def getAnagramKey(word):
                
                abc_counter = ["0"] * 26 # lowercase english alphabet array 
                for c in word:
                    
                    index = get_counter_index(c) # we can use ascii code
                    abc_counter[index] += 1
                
                return tuple(abc_counter) # key

            groups = map()

            for s in strs:
                
                key = getAnagramKey(s)
                if key is in map:
                    groups[key].add(s)
                else:
                    groups[key] = [s]

            res = []
            for group in groups:
                res.insert(group)
            return res
        """
        """ Efficiency
            m - a string
            n - number of strings
            helper function -> O(m) time and O(1) space
            main code -> O(n) time and O(n) space
            overall time and space:
                O(n*m)
                O(n) 
        """
        def getAnagramKey(word):
                
            abc_counter = [0] * 26 # lowercase english alphabet array 
            for c in word:
                
                index = ord(c) - ord('a') # ex1: a - a = 0; ex2: b - a = 1
                abc_counter[index] += 1
            
            return tuple(abc_counter) # key
        
        groups = {}
        
        for s in strs:
            key = getAnagramKey(s)
            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)

        return list(groups.values())

        











