class Solution:
	# @param A : string
	# @param B : string
	# @return a strings
	def addBinary(self, A, B):
        result = ""
        carry = 0
        
        A = list(A)
        B = list(B)
        
        while A or B or carry:
            bit_a = int(A.pop()) if A else 0
            bit_b = int(B.pop()) if B else 0
            
            current_sum = bit_a + bit_b + carry
            
            result = str(current_sum % 2) + result
            
            carry = current_sum // 2
        
        return result
