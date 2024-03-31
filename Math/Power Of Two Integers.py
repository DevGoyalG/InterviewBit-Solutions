class Solution:
	# @param A : integer
	# @return an integer
	def isPower(self, A):
		if A == 1:
            return 1
        
        max_exp = int(A**0.5)  
        
        for base in range(2, max_exp + 1):
            exponent = 2
            power = base ** exponent
            while power <= A:
                if power == A:
                    return 1
                exponent += 1
                power = base ** exponent
        return 0
