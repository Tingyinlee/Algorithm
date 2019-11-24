#!/usr/bin/env python
# coding: utf-8

# ＊理解binarary search tree過程參考資料：
# 1. http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
# 
# 2. 演算法圖鑑 by石田保輝 ＆ 宮崎修一
# 
# ＊程式碼：from老師提供下載的程式範例去做新增跟修改內容

# In[37]:


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
        if root is None:    #跟 search 相比 因為需要多紀錄 父節點 所以會再重新寫一次search
            return None

        if target == root.val:  #接下來 另外比對一下 需要刪除的 是不是 root
            
            #在這裡呢 我們分成幾種情況來看
            #當 沒有子節點  / 只有一個節點 / 有兩個子節點的情況
            if root.left is None and root.right is None:   #沒有子節點的時候 在這個情況下代表:只有root 這一個節點而且我們必須刪掉它
                return None
            elif root.left is None:    #左邊沒有
                return root.right
            elif root.right is None:   #右邊沒有
                return self.delete(root.left, target)   ##為了處理後方重複狀況，所以要遞迴(當只有左邊child的時候，我原本回傳 root.left 但這裡呢，我把這個root.left再拿去delete一次! 來確保說 我接上來的left 已經是刪除好的子樹)
            else:                           #兩邊都有
                #先從右邊找
                cur_node = root.right  #這時我們先走到右邊，然後一直往左走直到底
                parent_node = root 
                while cur_node.left:  #當左邊還有子節點時
                    parent_node = cur_node
                    cur_node = cur_node.left  #往左邊子節點走
                cur_node.left = self.delete(root.left, target)   ##為了處理後方重複狀況，所以要遞迴(當我們要把 root.left 接到 新的root 上的時候，同樣的把 root.left 外包給其他delete函式，幫我檢查左邊有沒有問題)
                if cur_node != root.right:  #當cur_node 不是 root.right 的時候，才把root右節點接上去
                    if cur_node.right: 
                            parent_node.left = cur_node.right
                    else:
                            parent_node.left = None   #將原本父節點左邊（子結點）位置的數字拿掉
                            cur_node.right = root.right
                else:   # 當cur_node 是 root.right 的時候
                            parent_node.left = None
                
            return cur_node
            
    
        elif target < root.val:
            if root.left:
                parent_node = root
                parent_node.left = self.delete(root.left, target)   #已經完成 delete 動作的 root.left 子樹的樹頭! (只要再把這個樹頭 接到 root.left 上面就完成了)
                return root
            else:
                return root
            
            
        elif target > root.val:
            if root.right:
                parent_node = root
                parent_node.right = self.delete(root.right, target)  
                return root
            else:
                return root
        
        # 接著要處理數字有 「重複」 的狀況 ， 已知同樣的數字會往左擺，所以只要處理if target == root.val: 左邊情形即可 
        #(可看 if target == root.val: 當中註解有兩個##的部分 )
        #因為 elif target < root.val: 裡面 我們 把 root.left 外包給 另外一個delete來做了
        #可以假設 另外一個delete幫我們把左邊的子樹已經刪除好了  ， 右邊也是一樣
        #那 一直外包 最後到底誰要做呢?
        #總會有個delete 運氣不好 剛好 接到  root 是 要刪除的數字 的 子樹
        #這時候就會由上面的code來處理了!
        
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
        if root is None: 
            return None
        
        modify_needed = self.count_val(root, target)  #這裡呢要來使用剛才寫的 放在下面的count_val
        if modify_needed == 0
            return None
        else:
            new_root = self.delete(root, target)  # 我們知道了有幾個需要修改的點，也把這些點都先移除了，再來呢 得把這些點加回去
            #知道了 數量 也知道新的值 那我可以用個for 迴圈 來做這件事
            for i in range(0, modify_needed):
                self.insert(new_root, new_val)
            return new_root
            
        
        # 計算有幾個點 val = target
    def count_val(self, root, target):
        #先檢查 root 有沒有東西 沒有的話 就返回 0
        if not root:
            return 0
        #左半邊的樹呢 我外包給另一個 count_val 來算
        else:
            left_count = self.count_val(root.left, target) #把左邊子樹 的 target數量回傳
        #右半邊 我也外包給其他count_val來算
            right_count = self.count_val(root.right, target)
            total = left_count + right_count
            if root.val == target:
                total = total + 1
            return total


# In[41]:





# In[ ]:




