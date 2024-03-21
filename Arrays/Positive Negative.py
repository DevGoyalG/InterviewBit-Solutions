class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        positive_count=0
        negative_count=0
        
        for num in A:
            if num>0:
                positive_count+=1
            elif num<0:
                negative_count+=1
        return [positive_count, negative_count]
