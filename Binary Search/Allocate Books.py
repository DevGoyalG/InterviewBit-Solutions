class Solution:
    def books(self, A, B):
        if len(A) < B:
            return -1
        
        def is_possible(max_pages):
            students = 1
            pages_read = 0
            for pages in A:
                if pages > max_pages:
                    return False
                if pages + pages_read > max_pages:
                    students += 1
                    pages_read = pages
                else:
                    pages_read += pages
            return students <= B
        
        low = max(A)
        high = sum(A)
        result = -1
        while low <= high:
            mid = (low + high) // 2
            if is_possible(mid):
                result = mid
                high = mid - 1
            else:
                low = mid + 1
        return result
