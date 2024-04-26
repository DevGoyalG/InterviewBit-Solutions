class Solution:
    # @param A : string
    # @param B : list of strings
    # @return a list of strings
    def wordBreak(self, A, B):
        word_set = set(B)
        def word_break_helper(s):
            if not s:
                return [[]]
            partitions = []
            for i in range(1, len(s) + 1):
                prefix, suffix = s[:i], s[i:]
                if prefix in word_set:
                    for partition in word_break_helper(suffix):
                        partitions.append([prefix] + partition)
            return partitions
        partitions = word_break_helper(A)
        sentences = [' '.join(partition) for partition in partitions]
        return sorted(sentences)
