    # @param A : tuple of integers
    # @return an integer
    def majorityElement(self, A):
        candidate = 0
        count = 0

        for num in A:
            if count == 0:
                candidate = num

            count += 1 if candidate == num else -1

        return candidate
