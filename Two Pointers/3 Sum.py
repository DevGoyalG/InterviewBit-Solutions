class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def threeSumClosest(self, A, B):
        A.sort() 
        closest_sum = float('inf') 
        
        for i in range(len(A)):  
            j, k = i + 1, len(A) - 1
            while j < k:  
                current_sum = A[i] + A[j] + A[k]  
                if abs(current_sum - B) < abs(closest_sum - B):  
                    closest_sum = current_sum
                
                if current_sum > B:  
                    k -= 1
                elif current_sum < B:
                    j += 1
                else:
                    return B  
            
        return closest_sum
