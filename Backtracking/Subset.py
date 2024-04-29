class Solution:
    # @param A : list of integers
    # @return a list of list of integers
    def subsets(self, A):
        A.sort()
        result = []
        self.generate_subsets(A, 0, [], result)
        return result
    
    def generate_subsets(self, A, index, current, result):
        result.append(current[:])
        
        for i in range(index, len(A)):
            current.append(A[i])
            self.generate_subsets(A, i + 1, current, result)
            current.pop()
