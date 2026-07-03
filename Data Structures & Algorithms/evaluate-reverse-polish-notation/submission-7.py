class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        ''' Translate
        return the result that is made by computing the arithmetic expression in RPN (Reverse Polish Notation) 
        '''

        ''' Requirements
        the return value must be an integer
        the RPN is always valid
        '''

        ''' Approach
        recognize a valid arithmetic expression in RPN using the help of a stack
        we push the numbers into the stack and when
            1. there are 2 numbers, expect an operator
                - perform the operation {number1 operator number2}
                - push the result back onto the stack
            2. there is 1 element left, expect either an operator or a number
                - push the number onto the stack
                - proceed with the operations in step 1
            
            visual example:
                tokens = ["1","2","+","3","*","4","-"]
                stack = [1]

                iteration 1:
                stack.push(i)
                stack = [1, 2]
                val = performOp(stack.pop(), stack.pop(), tokens[i])
                stack.push(val)
                stack = [3]

                iteration 2:
                stack = [3, 3]
                val = performOp(stack.pop(), stack.pop(), tokens[i])
                stack.push(val)
                stack = [9]

                iteration 3:
                stack = [9, 4]
                val = performOp(stack.pop(), stack.pop(), tokens[i])
                stack.push(val)       
                stack = [5]

                // end of tokens
                return stack[0] 
        '''

        ''' Code / Pseudocode
        tokens = ["1","2","+","3","*","4","-"]

        stack = [tokens[0]]

        for i in range(1, len(tokens)):
            
            stack.push(tokens[i]) // always becomes two consecutive numbers
            stack.push(performOp(stack.pop(), stack.pop(), op))
        
        return stack[0]

    def performOp(num2, num1, op):
        
        if op == "+":
            return num1 + num2
        if op == "-":
                return num1 - num2
        if op == "/":
                return num1 / num2
        if op == "*":
            res = num1 * num2
        else:
            return None
        '''

        stack = []

        for i in range(0, len(tokens)):
            
            t = tokens[i]
            if self.isOp(t):
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(self.performOp(num1, num2, t)))
            else:
                stack.append(int(t))
        
        return stack.pop()

    def performOp(self,num1, num2, op):
        
        if op == "*":
            return num1 * num2
        if op == "/":
            return num1 / num2 # requirement of integers truncating toward zero
        if op == "+":
            return num1 + num2 
        if op == "-":
            return num1 - num2
        
    def isOp(self, op):
        return op == "*" or op == "/" or op == "+" or op == "-"



