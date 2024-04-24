class Solution:
    # @param A : string
    # @return a strings
    def simplifyPath(self, A):
        stack = []
        directories = A.split('/')
        
        for directory in directories:
            if directory == '.' or directory == '':
                continue
            elif directory == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(directory)
        
        simplified_path = '/' + '/'.join(stack)
        
        return simplified_path
