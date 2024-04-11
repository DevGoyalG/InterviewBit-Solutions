class Solution:
    def subsetsWithDup(self, A):
        A.sort()  
        
        def backtrack(start, path, result):
            result.append(path[:]) 
            
            for i in range(start, len(A)):
                if i > start and A[i] == A[i - 1]:
                    continue
                path.append(A[i])
                backtrack(i + 1, path, result)
                path.pop()
        
        result = []
        backtrack(0, [], result)
        return result
