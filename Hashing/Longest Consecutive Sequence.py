class Solution:
	# @param A : tuple of integers
	# @return an integer
	def longestConsecutive(self, A):
		num_set = set(A)
        max_length = 0
        
        for num in A:
            if num - 1 not in num_set:
                current_num = num
                current_length = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                max_length = max(max_length, current_length)
        
        return max_length
