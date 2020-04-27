"""Design a stack that supports push, pop, top, and retrieving the minimum element in constant time."""

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_val = float('+inf')
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        self.min_val = min(x,self.min_val)
        

    def pop(self):
        """
        :rtype: None
        """
        print(self.stack)
        self.stack.pop()
        if self.stack:
            self.min_val = min(self.stack)
        else:
            self.min_val = float('+inf')
        

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]
        else:
            return []
        

    def getMin(self):
        """
        :rtype: int
        """        
        return self.min_val
        

if __name__ == "__main__":
    
    obj = MinStack()
    #["push","push","getMin","getMin","push","getMin","getMin","top","getMin","pop","push","push","getMin","push","pop","top","getMin","pop"]
#[[],[-10],[14],[],[],[-20],[],[],[],[],[],[10],[-7],[],[-7],[],[],[],[]]
    obj.push(-10)
    obj.push(14)
    obj.pop()
    obj.push(-20)
    obj.pop()
    obj.push(10)
    obj.push(-7)
    print(obj.stack)
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.getMin()
    print(param_4)