#A simple implementation of Stack abstract data type

class Stack(object):
    #Stack differs from a list in the way we are going to use it
    #Initiate a list to hold the values
    def __init__(self):
        self.list = []
        self.size = 0
    #Push a value onto a stack and increment size     
    def push(self, value):
        self.size += 1
        self.list.append(value)  
    #Take value out of the stack and return it and decrement the size    
    def pop(self):
        self.size -= 1
        return self.list.pop()  
    #Check if the stack is empty    
    def isEmpty(self):
        return self.size == 0
    #Check for the value that is at the top of the stack
    def peek(self):
        return self.list[self.size - 1]
    #Check the size of the stack
    def getSize(self):
        return self.size
#Tests   
s = Stack()
print s.isEmpty()
s.push(1)
s.push(3)
print s.pop()
s.push(2)
print s.peek()
print s.getSize()
print s.isEmpty()