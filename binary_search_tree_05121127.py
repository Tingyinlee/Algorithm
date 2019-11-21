#!/usr/bin/env python
# coding: utf-8

# ＊理解binarary search tree過程參考資料：
# 1. http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
# 
# 2. 演算法圖鑑 by石田保輝 ＆ 宮崎修一
# 
# ＊程式碼：from老師提供下載的程式範例去做新增跟修改內容

# In[ ]:


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
        """
        :type val: int
        :type left: TreeNode or None
        :type right: TreeNode or None
        """
class Solution(object):  #這裡的Solution 會直接加入 已經寫好的樹   Solution裡面不用自己留存任何資料
    self.root = None  #每個函式都會接收到需要處理的樹頭 也就是 root
    
    def insert(self, root, val):  #insert的input 是 root 跟 val 值
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode(inserted node)
        """
        if root is None:  #None == None 在有些函式庫當中 會是為不同東西 回傳 false
            newNode = TreeNode(val)  #要新建一個TreeNode出來。*另外： 放進去 就用(  )  / 拿出來 就用 .
            return newNode
        if val <= root.val:
            if root.left == None:
                newNode = TreeNode(val)
                root.left = newNode
                return root.left
            self.insert(root.left, val)
            
        elif val > root.val:
            if root.right == None:
                newNode = TreeNode(val)
                root.right = newNode
                return root.right
            self.insert(root.right, val)
            
        
        
    def delete(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(the root of new completed binary search tree) (cannot search())
        """
    def search(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode(searched node)
        """
        if root is None: 
            return None

        if target == root.val:
            return root
        elif target < root.val:
            return self.search(root.left, target)
        elif target > root.val:
            return self.search(root.right, target)
        
            
            
            
    def modify(self, root, target, new_val):
        """
        :type root: TreeNode
        :type target: int
        :type new_val: int
        :rtype:TreeNode(the root of new completed binary search tree) (cannot search())
        """

