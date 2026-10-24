""" Translation
    We are given a string to prove whether or not it is a palindrome.
"""

""" Requirements
    A palindrome is defined as a string that reads the same forward and backward. It also ignores
    all non-alphanumeric characters and will remain case-insensitive.
    The output of the function must return True or False.
"""

""" Approach
    Create a function to check whether the character is part of the palindrome or not -> 
    alphaNumericChar(str).
    Use pointers left and right to check each character at both ends.
    Since a palindrome is the same forwards and backwards; every valid pointer must match 
    up until the left equals or crosses the right index.
    i.e. the string "a" is a palindrome, because the left = 0 and right = 0.
    i.e. the string "aa" is a palindrome, because the left = 0 and right = 0.
"""

""" Psuedocode
    isAlphaNumericChar(str): # O(1)
        str is in the set of alphanumeric characters
        return true
    
    l = 0          # beginning index of string
    r = len(s) - 1 # end index of string

    # iterate the string
    while l <= r:

        # ignore all non-alphanumeric characters
        if isAlphaNumericChar(s[l]) == False:
           l += 1
           continue
        if isAlphaNumericChar(s[r]) == False:
            r -= 1
            continue
         
        if s[l] == s[r]:
            l -= 1
            r += 1
        else:
            return False # character mismatch
    
    return True # all characters were exhausted
        
"""

""" Efficiency
    The character validator uses a set so we remain at O(1).
    The while loop must exhaust the entire length of the string so we have O(n).
"""

class Solution:
    def isNumber(self, ch):
        """ Checks if a character is part of the number 0-9 """
        
        ascii_ch = ord(ch)

        return ascii_ch >= ord('0') and ascii_ch <= ord('9')

    def isAlphabet(self, ch): # O(1)
        """ Checks if a character is part of the alphabet """
        ascii_ch = ord(ch)

        # use ascii math to check for upper and lower-case letters
        if ascii_ch >= ord('A') and ascii_ch <= ord('Z'):
            return True
        if ascii_ch >= ord('a') and ascii_ch <= ord('z'):
            return True
        
        return False # not in the alphabet

    def isPalindrome(self, s: str) -> bool:
        
        l = 0          # beginning index of string
        r = len(s) - 1 # end index of string

        # iterate the string
        while l <= r:

            # ignore all non-alphanumeric characters
            if self.isAlphabet(s[l]) == False and self.isNumber(s[l]) == False:
                l += 1
                continue
            if self.isAlphabet(s[r]) == False and self.isNumber(s[r]) == False:
                r -= 1
                continue
            
            # check alphabetical letters
            if self.isAlphabet(s[l]) == True and self.isAlphabet(s[r]) == True:
                
                if s[l].lower() != s[r].lower():
                    return False    # character mismatch
                else:
                    l += 1
                    r -= 1
                    continue        # continue remaining string
            # check numbers 
            # (only option left since non-alphanumeric characters are gone and we checked alpahbet)
            if s[l] == s[r]:
                l += 1
                r -= 1
                continue
            else: 
                return False
        
        return True # all characters were exhausted
















