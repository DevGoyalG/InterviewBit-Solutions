class MinStack:
    def __init__(self):
        self.stack = []  
        self.min_stack = []  

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:  
            self.min_stack.append(x)

    def pop(self):
        if self.stack:
            top_element = self.stack.pop()
            if top_element == self.min_stack[-1]:  
                self.min_stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        return -1

    def getMin(self):
        if self.min_stack:
            return self.min_stack[-1]
        return -1
