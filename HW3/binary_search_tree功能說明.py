#!/usr/bin/env python
# coding: utf-8

# # 功能說明
# ＊理解binarary search tree過程參考資料：
# 1. http://alrightchiu.github.io/SecondRound/binary-search-tree-introjian-jie.html
# 
# 2. 演算法圖鑑 by石田保輝 ＆ 宮崎修一

# **以下的不同功能說明先後順序是按照我寫的時候的順序寫的: 新增 -> 搜尋 -> 刪除 -> 修改**

# 1. 新增insert的部分：
# 
#    如果一開始沒有找到root，就把值放入TreeNode，再放入新增的節點當中，然後回傳。
#    
#    如果有root:
#    
#    新增的值小於等於root的值時往左走，大於的話就往右，走到沒有root時就新增並回  
#    傳，若找不到的話就呼叫自己。

# 2. 搜尋search的部分：
# 
#    如果沒有找到root，就回傳None。
#    
#    有的root的話，有以下三種情況:
#    
#    1. 目標跟root值相等，就回傳root
#    
#    2. 目標值小於root值，就繼續往左走，找到或找不到為止。
#    
#    3. 目標值大於root值，就繼續往右走找，找到或找不到為止。

# 3. 刪除delete的部分：
# 
# 

# 4. 修改modify的部分：
# 
# 
