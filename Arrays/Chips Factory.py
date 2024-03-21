class Solution:
    # @param A : list of integers
    # @return a list of integers
    def solve(self, A):
        empty_packets = []

        for chip_count in A:
            if chip_count == 0:
                empty_packets.append(chip_count)
        
        A = [chip_count for chip_count in A if chip_count != 0]
        
        A.extend(empty_packets)
        
        return A
