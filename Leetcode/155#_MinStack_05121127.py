#!/usr/bin/env python
# coding: utf-8

# In[1]:


class MinStack(object):

    def __init__(self):
        self.s = []
        self.minVal = float("inf")

    def push(self, x):
        self.s.append(x)
        if x < self.minVal:
            self.minVal = x
            
    def updatemin(self):
        newMin = float("inf")
        for item in self.s:
            if item< newMin:
                newMin = item
        self.minVal =  newMin


    def pop(self):
        item = self.s.pop()
        if item == self.minVal:
            self.updatemin()
        return item

    def top(self):
        return self.s[-1]

    def getMin(self):
        return self.minVal


# In[ ]:




