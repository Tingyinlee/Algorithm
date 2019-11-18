#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class ListNode:
    def __init__(self, val):  #畫好每個節點長什麼樣
        self.val = val
        self.next = None
class MyLinkedList(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        cur_index = 0                  #一開始計數器是0
        cur_node = self.head           #我們身處列車頭
        while cur_node:                #當我走到的這個車廂是存在的時候
            if cur_index == index:     #比對我的計數器 跟 要找的車廂號碼 是不是一樣
                return cur_node.val    #拿出對應值回傳
            else:                      # 如果不一樣 那我要往下走
                cur_index += 1          # 計數器+1
                cur_node = cur_node.next  # 往下一節列車前進
                
        return -1
            

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        First_node = ListNode(val)
        if not self.head:
            self.head = First_node
        else:
            cur_head = self.head
            self.head = First_node
            First_node.next = cur_head

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            cur_node.next = new_node
    def addAtIndex(self, index, val): 
#別人要你幫忙在第index個添加值，要跟你說第幾個也就是 index，也要跟你說要加甚麼，也就是 val
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.  #首先呢 我們需要找到指定的index位置的車廂
           #然後 把 新的車廂 塞在這個位置 把 剩下的車廂 放在新車廂的後面
        :type index: int
        :type val: int
        :rtype: None
        """
        cur_index = 0     #找到指定的index位置 這個在get函式有寫過 一開始計數器是0
        cur_node = self.head 
        if index == 0:
            self.addAtHead(val)
        else:
            while cur_node:
                if cur_index == index -1:
                    new_node = ListNode(val)
                    old_index = cur_node.next
                    new_node.next = old_index
                    cur_node.next = new_node
                    break
                else:
                    cur_index += 1
                    cur_node = cur_node.next

                
    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        cur_index = 0
        cur_node = self.head
        if index == 0:           #前面砍掉車頭的情況 index == 0 我們已經處理掉了
            if self.head:
                self.head = self.head.next
        else:
            pre_node = self.head     #把上一個車廂先定為車頭
            while cur_node:
                if cur_index == index:
                    
                    if cur_node.next:  
                        # 當index車廂有後面的車廂的時候 把後面車廂 接給上一個車廂
                        pre_node.next = cur_node.next
                    else:     
                        # 當 index車廂 沒有後面的車廂 那把上一個車廂的接口拿掉
                        pre_node.next = None
                    break
                else:
                    cur_index += 1
                    pre_node = cur_node   
                    #在走到下一個車廂之前，先把車廂記錄起來，那就留下了上一個車廂的資訊了
                    cur_node = cur_node.next
                    
                    
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)


# 以上花費四小時完成，結果試跑一遍發現出現Time Limit Exceeded...
# 
# 代表他認為跑太久了，不過他例子只有幾個而已
# 
# 
# 所以應該是某一個while迴圈沒有正確結束

# 經過了將近二十分鐘的排查...
# 發現...原來是最後delete部分的最後一個else縮排錯誤...

# 結果按了submit之後還是噴了TLE...!
# def addAtIndex(self, index, val)
# 最後三行 else 的縮排
# 也要調整

# 結案：總共不眠不休花了四個半小時寫出來...太感動了阿...

# In[ ]:




