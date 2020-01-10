#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head):
        if head == None:
            return
        
        num = ''
        num += str(head.val)
        cur = head
        while cur.next != None:
            num += str(cur.next.val)
            cur = cur.next
        
        return int(num, 2)

