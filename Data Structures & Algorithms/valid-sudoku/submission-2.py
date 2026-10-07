# Translate
"""
    We are given a sudoku board to find out if it is following the given rules.
"""
# Requirements
"""
    The given order of rules:
        all elements are 1-9 or a dot character
        no duplicates in the row
        no duplicates in the columns
        no duplicates in the sub-boxes
    Return true or false
    Solve in O(n^2) time.
"""
# Approach
"""
    create a set of valid characters to compare the elements in the board to.
    create a function for each rule, such that every board is validated
    in the order of rules 1-3, and return true or false if one is violated.
    Rule 1-3: traverse a row and/orcolumn, for each element:
                validate the element, return false if it's invalid.
                add the non-empty element to a set, 
                return true if the set is unique, 
                otherwise, return false.
                ... Repeat for all rows.
"""
# Code / Pseudocode
"""
    valid_digit = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}
    valid_empty_char = "."

"""
# Efficiency
"""

"""
class Solution:

    empty_char = "."

    def isValidSudoku(self, board: List[List[str]]) -> bool:

        if self.isValidRule1(board) == False:
            return False
        if self.isValidRule2(board) == False:
            return False
        if self.isValidRule3(board) == False:
            return False
        
        return True

    def isValidRule1(self, board):
        """ Traverse every row to find duplicates """

        for row_index in range(len(board)):
            row_set = set()
            
            for element in board[row_index]:

                if self.isValidChar(element) == False:
                    return False
                if element in row_set:
                    return False
                if element != self.empty_char:
                    row_set.add(element)        
        return True
    
    def isValidRule2(self, board):
        """ Traverse every column to find duplicates """
        
        for i in range(len(board)):
            column_set = set()
            
            for j in range(len(board)):    
                element = board[j][i]
                
                if self.isValidChar(element) == False:
                    return False
                if element in column_set:
                    return False
                if element != self.empty_char:
                    column_set.add(element)  

        return True
    
    def isValidRule3(self, board):
        """ Traverse subboxes 0-8 to find duplicates """

        for i in range(len(board)):
            if self.isValidSubBox(board, i) == False:
                return False

        return True
    
    def isValidSubBox(self, board, box: int):
        """ Traverses a given box's elements to find duplicate """

        row, column = 3 * ((box) // 3), 3 * ((box) % 3)

        box_set = set()
        for i in range(row, row + 3):
            for j in range(column, column + 3):
                element = board[i][j]
                if self.isValidChar(element) == False:
                    return False
                if element in box_set:
                    return False
                if element != self.empty_char:
                    box_set.add(element)

        return True
    
    def isValidChar(self, element: str):
        """ Validates a given char to ensure it's a valid element """

        valid_char_set = {"1", "2", "3", "4", "5", "6", "7", "8", "9", "."}
        
        if element not in valid_char_set:
            return False
        
        return True
    
        