class Solution:
    # @param A : string
    # @param B : string
    # @return an integer
    def compareVersion(self, A, B):
        version1 = A.split('.')
        version2 = B.split('.')
        
        for i in range(max(len(version1), len(version2))):
            v1 = int(version1[i]) if i < len(version1) else 0
            v2 = int(version2[i]) if i < len(version2) else 0
            
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
        
        return 0
