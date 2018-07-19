class MaxQueue:
    
    def __init__(self):
        self.queue = []
        self.maxQueue = []
        
    def push(self, x):
        self.queue.append(x)
        while self.maxQueue and x >= self.maxQueue[-1]:
            self.maxQueue.pop()
        self.maxQueue.append(x)
        
    def pop(self):
        if not self.queue or not self.maxQueue:
            return
        
        result = self.queue.pop(0)
        if result == self.maxQueue[0]:
            self.maxQueue.pop(0)
        return result
    
    def getMax(self):
        return self.maxQueue[0]
        
    def peek(self):
        return self.queue[0]


MQueue = MaxQueue()
MQueue.push(1)
MQueue.getMax()
MQueue.push(2)
MQueue.getMax()
MQueue.push(4)
MQueue.push(5)
MQueue.pop()
MQueue.getMax()