class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, a, b):
        while b:
            a, b = b, a % b
        return a

    def cpFact(self, A, B):
        X = A  
        while self.gcd(X, B) != 1:  
            X = X // self.gcd(X, B)
        return X 
