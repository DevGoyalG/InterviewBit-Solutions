class Solution:
	# @param A : list of strings
	# @return an integer
	def evalRPN(self, A):
        stack = []

        for token in A:
            if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
                stack.append(int(token))
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()

                if token == "+":
                    stack.append(operand1 + operand2)
                elif token == "-":
                    stack.append(operand1 - operand2)
                elif token == "*":
                    stack.append(operand1 * operand2)
                elif token == "/":
                    stack.append(int(operand1 / operand2))

        return stack[0] if stack else 0
