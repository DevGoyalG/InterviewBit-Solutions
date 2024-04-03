class Solution:
    # @param A : string
    # @param B : integer
    # @return a list of integers
    def findPerm(self, A, B):
        result = []
        min_num = 1
        max_num = B
        
        for char in A:
            if char == 'I':
                result.append(min_num)
                min_num += 1
            elif char == 'D':
                result.append(max_num)
                max_num -= 1
        
        result.append(min_num)
        
        return result
