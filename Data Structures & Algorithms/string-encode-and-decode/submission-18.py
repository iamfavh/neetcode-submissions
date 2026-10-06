# Translate
"""
    We are given a list of strings to package into a single string that
    will be retrieved by another caller.
"""
# Requirements
"""
    The function needs to process 100 strings.
"""
# Approach
"""
    We can embed an instruction into the string, such that,
    - the caller can retrieve the list of strings
    - the list of strings are unchanged
"""
# Code / Pseudocode
"""
    encode(strs)
        create a new string res
        for each str s in strs
            prepend the length to s
            append s to res
        return res
    decode(s)
        create a new list res
        i = 0
        while i != len(s)
            word_length = s[i] # amount to extract from s
            if word_length == 0
                i++
                skip
            # extract word
            new_word = s[i+1:word_length]
            res.append(new_word)
            i += word_length + 1
"""
# Efficiency
"""

"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        """ returns a string with pre-pended amount and delimiter '#' for every string """
        
        res = ""

        for s in strs:
            formatted_s = f"{len(s)}#{s}"
            res = f"{res}{formatted_s}"

        return res

    def decode(self, s: str) -> List[str]:
        """ extracts strings from a payload with <length_string>#string format. """
        
        res = []
        i = 0

        delimiter = "#"

        
        while True:
            
            s_length = self.extract_length(s[i:])
            
            if s_length is None:
                return res

            format_promise = len(str(s_length)) + len(delimiter)

            if s_length == 0:
            
                res.append("")
                i += format_promise
                continue
            
            start_index = i + format_promise
            end_index = start_index + s_length
            word = s[start_index:end_index]
            res.append(word)

            i = end_index

        return res


    def extract_length(self, s):

        str_res = ""

        for c in s:
            
            if c == '#':
                return int(str_res)

            str_res = f"{str_res}{c}"
        
        # s is empty
        return None
            
