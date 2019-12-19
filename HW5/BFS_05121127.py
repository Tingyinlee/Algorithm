#!/usr/bin/env python
# coding: utf-8

# ＊理解BFS＆DFS過程參考資料：
# 1. http://alrightchiu.github.io/SecondRound/graph-breadth-first-searchbfsguang-du-you-xian-sou-xun.html
# 2. http://alrightchiu.github.io/SecondRound/graph-depth-first-searchdfsshen-du-you-xian-sou-xun.html
# 
# 3. 演算法圖鑑 by石田保輝 ＆ 宮崎修一
# 
# ＊程式碼：from老師提供下載的程式範例去做新增跟修改內容 http://codepad.org/bIExbqAn

# In[5]:


from collections import defaultdict 

class Graph:
    
    def __init__(self): 
        
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
    
                         
    def BFS(self, s): 
        """
        :type s: int
        :rtype: list
        """
        visited_list = []
        wish_list = [] 
        wish_list.append(s)
        
        while wish_list:
            cur_node = wish_list.pop(0) 
            visited_list.append(cur_node)  
            for next_level_node in self.graph[cur_node]:
                if not (next_level_node in visited_list or next_level_node in wish_list):  
                    wish_list.append(next_level_node) 
        
        return visited_list                         
        
        
    def DFS(self, s):
        """
        :type s: int
        :rtype: list
        """
        visited_list = []
        wish_list = []
        wish_list.append(s)
        
        while wish_list:
            cur_node = wish_list.pop() 
            visited_list.append(cur_node)
            for next_level_node in self.graph[cur_node]:
                if not (next_level_node in visited_list or next_level_node in wish_list):
                    wish_list.append(next_level_node)
        
        return visited_list
  


# In[6]:


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)


print(g.BFS(2))
print(g.DFS(2))


# In[ ]:




