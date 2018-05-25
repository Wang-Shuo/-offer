# -*- coding:utf-8 -*-

class ListNode:
    def __init__(self, x=None):
        self.val = x
        self.next = None

class Solution1:
    def printListReversingly(self, listNode):
        if listNode.val == None:
            return
        l = []
        head = listNode
        while head:
            l.insert(0, head.val)
            head = head.next
        return l

class Solution2:
    def printListReversingly(self, listNode):
        l = []
        head = listNode
        while head:
            l.append(head.val)
            head = head.next
        l.reverse()
        return l

node1 = ListNode(10)
node2 = ListNode(11)
node3 = ListNode(13)
node1.next = node2
node2.next = node3

singleNode = ListNode(12)

test = ListNode()

S = Solution2()
print(S.printListReversingly(node1))
print(S.printListReversingly(test))
print(S.printListReversingly(singleNode))
