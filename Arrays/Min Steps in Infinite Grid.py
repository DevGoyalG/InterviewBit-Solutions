class Solution:
    # @param A : list of integers
    # @param B : list of integers
    # @return an integer
    def coverPoints(self, A, B):
        if len(A) <= 1:
            return 0
        
        total_steps = 0
        for i in range(1, len(A)):
            steps_x = abs(A[i] - A[i - 1])
            steps_y = abs(B[i] - B[i - 1])
            total_steps += max(steps_x, steps_y)
        
        return total_steps
