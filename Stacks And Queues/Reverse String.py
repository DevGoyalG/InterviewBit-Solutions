class Solution:
	# @param A : string
	# @return a strings
	def reverseString(self, A):
        stack = []
        for char in A:
            stack.append(char)
        
        reversed_string = ""
        
        while stack:
            reversed_string += stack.pop()
        
        return reversed_string
