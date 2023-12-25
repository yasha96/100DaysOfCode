class Solution(object):
    def calPoints(self, operations):
        stack = []
    
        for op in operations:
            if op.isdigit() or op[0] == '-':
                stack.append(int(op))
            elif op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
    
        return sum(stack)

# Example usage:
operations = ["5","2","C","D","+"]
solution = Solution()
print(solution.calPoints(operations))
