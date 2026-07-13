class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0] * len(temperatures)
        stack = []
        i = 0
        for t in temperatures:
            
            if len(stack) == 0:
                stack.append((t, i))
            
            elif t > stack[-1][0]: 
                temp_and_index_tuple = stack.pop()
                index = temp_and_index_tuple[1]
                diff = i - index 
                result[index] = diff

                while len(stack) != 0 and t > stack[-1][0]:
                    temp_and_index_tuple = stack.pop()
                    index = temp_and_index_tuple[1]
                    diff = i - index
                    result[index] = diff
                
                stack.append((t,i))

            else:
                stack.append((t,i))

            i += 1

        return result

        """ Notes
            after 
            iter 1: stack = [(30,0)], result = [0,0,0,0,0,0,0], i=1
            iter 2: stack = [(38,1)], result = [1,0,0,0,0,0,0], i=2
            iter 3: stack = [(38,1),(30,2)], result = [1,0,0,0,0,0,0], i=3
            iter 4: stack = [(38,1),(36,3)], result = [1,0,1,0,0,0,0], i=4
            iter 5: stack = [(38,1),(36,3), (35,4)], result = [1,0,1,0,0,0,0], i=5
            iter 6: stack = [(40,5)], result = [1,4,1,2,1,0,0], i=6
            iter 7: stack = [(40,5),(28,6)], result = [1,4,1,2,1,0,0], i=7
        """




