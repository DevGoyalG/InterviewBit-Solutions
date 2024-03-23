class Solution:
    # @param A : string
    # @return an integer
    def isPalindrome(self, A):
        def is_alphanumeric(c):
            return c.isalnum()
        
        A = A.lower()
        left, right = 0, len(A) - 1
        
        while left < right:
            while left < right and not is_alphanumeric(A[left]):
                left += 1
            while left < right and not is_alphanumeric(A[right]):
                right -= 1
            
            if A[left] != A[right]:
                return 0
            
            left += 1
            right -= 1
        
        return 1
