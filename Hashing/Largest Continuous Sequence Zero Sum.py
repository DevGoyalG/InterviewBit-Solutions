class Solution:
    # @param A : list of integers
    # @return a list of integers
    def lszero(self, A):
        sum_dict = {0: -1}
        max_length = 0
        start_index = -1
        end_index = -1
        cumulative_sum = 0
        
        for i in range(len(A)):
            cumulative_sum += A[i]
            
            if cumulative_sum in sum_dict:
                if i - sum_dict[cumulative_sum] > max_length:
                    max_length = i - sum_dict[cumulative_sum]
                    start_index = sum_dict[cumulative_sum] + 1
                    end_index = i
            else:
                sum_dict[cumulative_sum] = i
        
        if start_index != -1:
            return A[start_index:end_index+1]
        else:
            return []
