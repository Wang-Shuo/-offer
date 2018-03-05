# -*- coding:utf-8 -*-
# use two stacks to implement a queue
class Solution:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, node):
        self.stack1.append(node)
    def pop(self):
        if len(self.stack1) == 0 and len(self.stack2) == 0:
            return
        elif len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


# use two queues to implement a stack
class Solution1:
    def __init__(self):
        self.queue1 = []
        self.queue2 = []
    def push(self, x):
        if len(self.queue2) == 0:
            self.queue1.append(x)
        else:
            self.queue2.append(x)
    def pop(self):
        if len(self.queue1) == 0 and len(self.queue2) == 0:
            return
        if len(self.queue1) != 0:
            len1 = len(self.queue1)
            for i in range(len1 - 1):
                self.queue2.append(self.queue1.pop(0))
            return self.queue1.pop()
        else:
            len2 = len(self.queue2)
            for i in range(len2 - 1):
                self.queue1.append(self.queue2.pop(0))
            return self.queue2.pop()

# test
Queue = Solution()
Queue.push(10)
Queue.push(11)
Queue.push(12)
print(Queue.pop())
Queue.push(13)
print(Queue.pop())
print(Queue.pop())
print(Queue.pop())
print(Queue.pop())


Stack = Solution1()
Stack.push(10)
Stack.push(11)
Stack.push(12)
print(Stack.pop())
Stack.push(13)
print(Stack.pop())
print(Stack.pop())
print(Stack.pop())
print(Stack.pop())
