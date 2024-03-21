class Solution:
    # @param A : list of integers
    # @return an integer
    def solve(self, A):
        MOD=10**9 + 7
        old_count=0
        
        for n in A:
            if n%2==1:
                old_count+=1
                
        result=pow(2, old_count, MOD) - 1
        return result%MOD
