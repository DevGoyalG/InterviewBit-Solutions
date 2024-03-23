class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        stack = []
        count = 0
        
        for char in A:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    count += 1
        
        return len(stack) + count
