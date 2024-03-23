class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        freq_arr=[0] * 26
        for char in A:
            index = ord(char) - ord('a')
            freq_arr[index] += 1
        return freq_arr
