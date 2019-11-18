#!/usr/bin/env python
# coding: utf-8

# In[130]:


def mergeSort(unsorted_list):
        if len(unsorted_list) == 1: #如果數入的串列中只有一個數字
            return(unsorted_list)
        elif len(unsorted_list) >1:
         midlen = len(unsorted_list)//2
         left = mergeSort( unsorted_list[:midlen]  ) #呼叫函式
         right = mergeSort(unsorted_list[midlen:] )
         len(unsorted_list) == 1
         i = j = 0
         answer_list = []
         while i + j < len (unsorted_list):
                if i >= len(left):  #判斷 i 是不是出界於本身長度，超過就把right list擺上去加到後面
                    answer_list.extend(right[j : ])
                    break
                if j >= len(right):
                    answer_list.extend(left[i : ])
                    break
                if left[i] >= right[j]:
                      answer_list.append(right[j])
                      j = j+1
                elif left[i] < right[j]:
                      answer_list.append(left[i])
                      i = i+1
        return answer_list


# In[131]:


print (mergeSort([4,3,2,1]))


# In[132]:


print (mergeSort([4,3,2]))


# In[133]:


print (mergeSort([6, 4, 3, 7, 5, 1, 2]))


# In[134]:


print (mergeSort([2]))


# 很好，寫到套上遞迴前我已經花了兩小時又十三分鐘 ^_^
# 整個寫出來到用數字去測試程式正不正確又花了一個半小時...

# In[ ]:




