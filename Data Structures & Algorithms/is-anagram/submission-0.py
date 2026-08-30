class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        
        """ Problem
                Two strings that may look different but contain the same
            characters are Anagrams of each other.
                The strings consist of only English lowercase letters 
            Find out whether they are anagrams of each other.
        """
        """ Requirements
            Do:
                return True or False
            Don't:
                accept empty strings
                accept strings > 5 * 10^4
        """
        """ Approach
            We obtain the count of each letter in the 1st word and add it to an array 
            that represents the lowercase alphabet, then subtract the count of each letter
            in the 2nd word. The words are anagrams of each other if the array results in 0s.
            To represent the letters in an array, we'll use ASCII values to increment or
            decrement a-z.
        """
        """ Pseudocode

            # if the words don't match in size, return False immediately 
        
            abc = [0] * 26 # alphabet counter

            # traverse the first word, increment the letters it contains
            for ch in s:
                
                getIndexOfLetter
                incrementCountAtIndex
            
            for ch in t:

                getIndexOfLetter
                decrementCountAtIndex
            
            return !abc.contains(0)
        """

        abc = [0] * 26

        for ch in s:

            index = ord('a') - ord(ch)
            abc[index] += 1
        
        for ch in t:

            index = ord('a') - ord(ch)
            abc[index] -= 1
        
    
        for count in abc:
            if count != 0:
                return False
        
        return True
        









