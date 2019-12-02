#!/usr/bin/env python
# coding: utf-8

# 了解Hash流程圖及原理的參考資料：
# 1. 演算法圖鑑 by石田保輝 ＆ 宮崎修一
# 2. 老師上課的PPT參考內容：
#     https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash
# 
# Code designed & changed from: http://codepad.org/0LBDUdlF

# In[47]:


from Crypto.Hash import MD5

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        """
        :type val: int
        :type next: ListNode
        :rtype: None        
        """
class MyHashSet:
    def __init__(self, capacity=5):
        self.capacity = capacity
        self.data = [None] * capacity  #是在初始化一個 長度為 capacity 內容物為None 的array
        """
        :type capacity: int
        :rtype: None
        """
    
    def get_MD5_int(self, key): #把取hash的部分寫在這個函式，接下來要用的時候就直接呼叫這個函式就可以了
        h = MD5.new()
        h.update(key.encode())  #h.update()輸入的資料格式是 byte，但是目前key是string，因此需要在轉換一次 python裡面string 使用.encode() 就可以把string轉乘byte了
        return int(h.hexdigest(), 16) #先把16進位數字 轉成10進位並用 int儲存之後 就回傳
    
    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        md5_num = self.get_MD5_int(key)  #剛剛寫了 get_MD5_int()函式 這邊直接拿來取得 10進位的數字
        data_loc = md5_num % self.capacity #有數字之後 我直接除以capacity 取餘數 就可以知道 我要放資料的格子是第幾格了

        #empty slot
        if not self.data[data_loc]: #確認這個格子裡面 有沒有放東西
            new_node = ListNode(md5_num)
            self.data[data_loc] = new_node
        #collision happened 
        else:
            cur_node = self.data[data_loc]
            while cur_node.next:
                cur_node = cur_node.next
            new_node = ListNode(md5_num)
            cur_node.next = new_node
        

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        md5_num = self.get_MD5_int(key)
        data_loc = md5_num % self.capacity  #拿到位置
        
        cur_node = self.data[data_loc]  # 承上面code 指定head為cur_node
        #1st link list 處理當頭需要換掉時的情境  
        if cur_node and cur_node.val == md5_num:  #若沒有頭 代表不用delete 當數字相等時 我們需要把頭換掉
            new_head = cur_node.next # 把頭的下一個指定為new_head 
            # if multiple node need to remove at 1st link list
            while new_head and new_head.val == md5_num:  #有可能有重複的情況 若有重複的情況 刪到有符合條件的點當new head為止
                new_head = new_head.next
            self.data[data_loc] = new_head # 把new_head接回 data

        #from 2nd link list to the end  處理完頭之後 再來從第二個開始往下刪
        cur_node = self.data[data_loc]  #重新指定一次頭
        while cur_node and cur_node.next: #如果next還有東西
            if cur_node.next.val == md5_num:  #如果下一個點的數值有比對到
                remain_node = cur_node.next.next #留下來的點就指定到next的next
                while remain_node and remain_node.val == md5_num:  #處理重複比對情況直到沒有重複
                    remain_node = remain_node.next 
                #get final remain_node 
                cur_node.next = remain_node #把被刪掉點的next接到前一個點cur_node後面

                cur_node = cur_node.next #當前處理的節點往後一個


    def contains(self, key):  #這邊跟add一樣，已經知道從data裡面第幾個開始找，不ㄧ樣的地方是：每走到一個就要比對一次，如果有了就可直接回傳
        """
        :type key: int
        :rtype: bool(True or False)
        """
        md5_num = self.get_MD5_int(key)
        data_loc = md5_num % self.capacity
        
        
        #if not self.data[data_loc]:
            #return False
        #else:     #有list的情況
            #cur_node = self.data[data_loc] #先把list的頭叫做cur_node 當前位置
            #while cur_node is not None: # 當cur_node還有東西，代表list還沒比完
                #if cur_node.val == md5_num: #如果比對到一致的話
                    #return True
                #cur_node = cur_node.next #每比完一次 就往下一個走
                
            #會走到這邊 代表跳出while迴圈 把整個list都走完了 比完了整個list都沒比對到
            #return False

        #slot non-empty
        cur_node = self.data[data_loc]
        while cur_node:
            if cur_node.val == md5_num:
                return True
            cur_node = cur_node.next
        return False
        


# In[48]:


hashSet = MyHashSet()
hashSet.add("dog")
hashSet.add("pig")
rel = hashSet.contains("pig")
print(rel)
rel = hashSet.contains("dog")
print(rel)
rel = hashSet.contains("cat")
print(rel)
hashSet.add("bird")
rel = hashSet.contains("bird")
print(rel)
hashSet.remove("pig")
rel = hashSet.contains("pig")
print(rel)


# In[ ]:




