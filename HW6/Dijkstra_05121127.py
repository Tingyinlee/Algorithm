#!/usr/bin/env python
# coding: utf-8

# ＊理解Minimum Spanning Tree ＆ Shortest Path 過程參考資料：
# 1. Dijkstra: http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html
# 2. Kruskal: http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html
# 
# 3. 演算法圖鑑 by石田保輝 ＆ 宮崎修一
# 
# ＊程式碼：from老師提供下載的程式範例去做新增跟修改內容 http://codepad.org/SlbGYd07

# In[1]:


# Python program for Dijkstra's single  
# source shortest path algorithm. The program is  
# for adjacency matrix representation of the graph 
# Python program for Kruskal's algorithm to find 
# Minimum Spanning Tree of a given connected,  
# undirected and weighted graph 

from collections import defaultdict 

#Class to represent a graph 
class Graph(): 

    def __init__(self, vertices): 
        self.V = vertices #總數
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
        self.cand_edge = {}
        
    def addEdge(self,u,v,w): 
        """
        :type u,v,w: int
        :rtype: None
        """
        self.cand_edge[ (u, v) ] = w
        
    def Dijkstra(self, s):  #s是起點
        """
        :type s: int
        :rtype: dict
        """
        shortest_dict = {} #建一個dictionary 把所有的點都加入
        cand_path = {} #
        shortest_dict[s] = self.graph[s][s]  #預作準備：把 graph當中 從 s 點 到 s點的 cost 放進最小cost路徑的dict當中
        
        for j in range(0, self.V):
            if self.graph[s][j] > 0:
                cand_path[ (s, j) ] = shortest_dict[s] + self.graph[s][j]  #起點終點包起來當key值
                
        while(len(shortest_dict.keys()) <  self.V): #判斷 dictionary的key值 數量是不是有到self.V
            shortest_val = float('inf') 
            shortest_pair = ""
            for node_pair in cand_path.keys():
                if cand_path[node_pair] < shortest_val and node_pair[1] not in shortest_dict.keys():
                    shortest_val = cand_path[node_pair]
                    shortest_pair = node_pair
            shortest_dict[shortest_pair[1]] = shortest_val  #取出終點 新加入shortest_dict
            del cand_path[shortest_pair]
            
            for j in range(0, self.V):
                if self.graph[shortest_pair[1]][j] > 0 and j not in shortest_dict.keys():
                    cand_path[(shortest_pair[1], j)] = shortest_dict[shortest_pair[1]] + self.graph[shortest_pair[1]][j]
                
        
        return shortest_dict
        
    def Kruskal(self):
        """
        :rtype: dict
        """
        united_island_list = [] #各個團結的島們
        for i in range(0, self.V):
            united_island_list.append([i])
            
        edge_dict = {}
        
        for pair, value in  sorted(self.cand_edge.items(), key= lambda x : x[1]):  #把所有可以蓋的橋 按價錢 由小到大排好
        
                pair_0_party = -1
                pair_1_party = -1
                for i in range(0, len(united_island_list)):
                    if pair[0] in united_island_list[i]:
                        pair_0_party = i
                    if pair[1] in united_island_list[i]:
                        pair_1_party = i
                        
                if pair_0_party != pair_1_party and pair_0_party != -1: #這裡比對是否同一個聯盟
                    merge_party = united_island_list.pop( pair_1_party )
                    united_island_list[pair_0_party].extend(merge_party)
                    edge_dict[ "{}-{}".format(pair[0],pair[1]) ] = value
                
        return edge_dict
            
            


# In[2]:


#測資：
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
             [4, 0, 8, 0, 0, 0, 0, 11, 0],
             [0, 8, 0, 7, 0, 4, 0, 0, 2],
             [0, 0, 7, 0, 9, 14, 0, 0, 0],
             [0, 0, 0, 9, 0, 10, 0, 0, 0],
             [0, 0, 4, 14, 10, 0, 2, 0, 0],
             [0, 0, 0, 0, 0, 2, 0, 1, 6],
             [8, 11, 0, 0, 0, 0, 1, 0, 7],
             [0, 0, 2, 0, 0, 0, 6, 7, 0],
             ];
print("Dijkstra",g.Dijkstra(0))

g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print("Kruskal",g.Kruskal())


# In[ ]:




