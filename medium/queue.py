# Implement a queue using two stacks. Process the following queries: 1 x -enqueue, 2-dequeue, 3-print.
# problem from CTCI 

class MyQueue(object):
    def __init__(self):
        self.first = []
        self.second = []
    
    def peek(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        return self.second[-1]
        
    def pop(self):
        if not self.second:
            while self.first:
                self.second.append(self.first.pop())
        #print self.first, self.second
        return self.second.pop()
        
    def put(self, value):
        self.first.append(value)
        

queue = MyQueue()
values = [(1, 42), (2, 0), (1, 14), (3, 0), (1, 28), (3, 0)]

for line in values:
    
    if line[0] == 1:
        queue.put(line[1])        
    elif line[0] == 2:
        queue.pop()
    else:
        print queue.peek()




        