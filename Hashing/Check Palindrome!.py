class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        char_freq = {}
        for char in A:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        odd_count = 0
        for freq in char_freq.values():
            if freq % 2 != 0:
                odd_count += 1

        if odd_count <= 1:
            return 1
        else:
            return 0
