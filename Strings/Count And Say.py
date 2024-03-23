class Solution:
	# @param A : integer
	# @return a strings
	def countAndSay(self, A):
        if A == 1:
            return "1"
        
        sequence = "1"
        
        for _ in range(2, A + 1):
            new_sequence = ""
            count = 1
            
            for i in range(1, len(sequence)):
                if sequence[i] == sequence[i - 1]:
                    count += 1
                else:
                    new_sequence += str(count) + sequence[i - 1]
                    count = 1
            
            new_sequence += str(count) + sequence[-1]
            
            sequence = new_sequence
        
        return sequence
