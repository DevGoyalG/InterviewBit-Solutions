class Solution:
	# @param A : integer
	# @return an integer
	def isPalindrome(self, A):
        if A < 0:
            return 0
        
        original_number = A
        reversed_number = 0

        while A > 0:
            digit = A % 10
            reversed_number = reversed_number * 10 + digit
            A = A // 10
            
        if reversed_number == original_number:
            return 1
        else:
            return 0
