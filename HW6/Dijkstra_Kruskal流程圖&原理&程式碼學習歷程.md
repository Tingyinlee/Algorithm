
了解Hash流程圖及原理的參考資料：
1. 演算法圖鑑 by石田保輝 ＆ 宮崎修一

2. Dijkstra原理參考：

   >a. http://alrightchiu.github.io/SecondRound/single-source-shortest-pathdijkstras-algorithm.html                                                                   
   >b. https://zh.wikipedia.org/wiki/戴克斯特拉算法
    
    
3. Kruskal原理參考：

   >a. http://alrightchiu.github.io/SecondRound/minimum-spanning-treekruskals-algorithm.html  
   >b. https://zh.wikipedia.org/wiki/克鲁斯克尔演算法                
   >c. https://www.itread01.com/content/1549869855.html
   
   
4. 老師上課的PPT參考內容：

    >a. https://docs.google.com/presentation/d/e/2PACX-1vTorNDEyhYA4ZAt5jEqOmFs2cQiUAYvkTp-R0DOn9B3c1MuUecV-a1wNakFIrJxA6AoUFGzbl3OQBIJ/pub?start=false&loop=false&delayms=3000&slide=id.p             
    >b. https://docs.google.com/presentation/d/e/2PACX-1vTgHO5AkHJS6iN6bnnBMMdHv6E4rabnrC0KwyTRfjad8Ab3IQjbnGvZuQOjDC9t7nKqeroiwcuasJrI/pub?start=false&loop=false&delayms=3000&slide=id.p

# Shortest Path (Dijkstra) & Minimum Spanning Tree (Kruskal) 流程圖：

[] (https://raw.githubusercontent.com/Tingyinlee/Algorithm/master/Pictures/5.jpg)

### Dijkstra steps:

>STEP.1
>1. 首先將圖轉成矩陣，如果是走到自己距離為0 ; 無法走到的點為無限∞。
>2. 選擇起始點 “1”。
>3. 標記 “1” 到個點的距離。
>4. 將第 1 欄位標記為「已計算出最小距離」的記號，起始點到 “1” 的最小距離為0。

>STEP.2
>1. 從第一列中除了已被標記為「以計算出最小距離」的點外，選擇離起始點最近的點“2”。
>2. 新增（1, 2）列，更新（1, 2）列的數值。如果加入 “2” 後，從起始點“1” 到其他點的距離相對沒有加入“2” 還短則更新數值。

>STEP.3
>1. 不斷重複STEP.2
>2. 新增（1, 2, 4, 5）列，更新 1~4 列的數值。如果加入 “5” 後，從起始點“1” 到其他點的距離相對沒有加入“5” 還短則更新數值。**其中 “3” 距離起始點的距離從5縮短為4。**

>STEP.4
>1. 不斷重複以上步驟直到所有點走過，沒有更新的數值為止。

### Kruskal steps:

>STEP.1
>1. 新建圖，圖中擁有原圖中相同的點，但沒有邊。
>2. 將各邊線依權值大小由小到大排列。

>STEP.2
>1. 從權值中權值最小的邊開始，如果這條邊連接的兩個節點於圖中不在同一個連通分量中，則添加這條邊到圖中。

>STEP.3
>1. 重複3，直至圖中所有的節點都在同一個連通分量中
>2. **＊注意：** 若有構成環的狀況(像是流程圖中 Example.2 abe / abce / abcde)就要跳過

>STEP.4
>1. 不斷重複以上步驟直到所有點走過，標記長度為5的bc，得到最小生成樹，結束演算法過程。


# Dijkstra & Kruskal 原理：

### Shortest Path (Dijkstra): 
該方法用於計算由某個頂點到其他頂點的最短路徑。
Dijkstra algorithm 和 Bellman-Ford algorithm一樣，都是用以解決最短路徑問題的演算法，求出從起點到終點之間，邊權重總和最小的路徑。

>[小知識：]
這個演算法的名稱，得名自開發者艾茲赫爾・戴克斯特拉 (Edsger Wybe Dijkstra) 。他在1972年獲頒圖靈獎 (Turing Award)。

>[解說：]
相較於對所有的邊進行權重計算和更新的貝爾曼-福特演算法，戴克斯特拉演算法注重於選擇頂點，進而有效率地求出最短路徑。
假設輸入圖形的點點數為n、邊數為m，未仔細研究選好頂點時的執行時間是O(n⌃2) ; 能夠對資料結構下功夫的話，執行時間能壓縮到O(m + n log n)。

>**補充：迴圈中有負權中時並不存在最短路徑。貝爾曼-福特演算法可以判定出最短路徑不存在，但就算最短路徑不存在，戴克斯特拉演算法也會將錯誤的最短路徑當作正確答案。因此，戴克斯特拉演算法無法用於有負權重的圖形。

*＊總結來說：如果邊沒有負權重，選擇執行時間較短的戴克斯特拉演算法較佳 ; 邊有負權重時，則選用執行時間雖然較長，卻可以正確求解的貝爾曼-福特演算法*

> For Example:
想要知道從高雄到台南，如果開車的話，通常會利用查詢的交通網路來取得: 最 短路徑或者走哪一條路最符合經濟效益。諾以圖形網路來思考，就是任意兩個頂 點之間的最短路徑或最少花費。
***
###  Minimum Spanning Tree (Kruskal): 
Kruskal演算法是一種用來尋找最小生成樹的演算法。
Kruskal Algorithm 為建立 MST 的其中一種方法。該演算法將各邊線依權值大小由 小到大排列，從權值最低的邊線開始架構 MST，依序拿最小成本的邊來搭建 MST， 如果加入的邊線會造成迴路則捨棄不用，直到加入了|V|−1 條邊線為止。

>[小知識：]
由Joseph Kruskal在1956年發表。用來解決同樣問題的還有Prim演算法和Boruvka演算法等。三種演算法都是貪婪演算法的應用。和Boruvka演算法不同的地方是，Kruskal演算法在圖中存在相同權值的邊時也有效。

>[解說：什麼叫最小生成樹？ ]
已知一個無向連通圖，那麼這個圖的最小生成樹是該圖的一個子圖，且這個子圖是一棵樹且把圖中所有節點連線到一起了。一個圖可能擁有多個生成樹。一個帶權重的無向連通圖的最小生成樹（minimum spanning tree），它的權重和是小於等於其他所有生成樹的權重和的。 
生成樹的權重和，是把生成樹的每條邊上的權重加起來的和。

一顆最小生成樹有多少條邊？ 
已知帶權重無向連通圖有V個節點，那麼圖的最小生成樹的邊則有V-1條邊。

> For Example:
MST 有很多實際應用，將網路頂點看做城市，邊看做連線城市的通訊網，邊的權重看做連線城市的通訊線路的成本，根據最小生成樹建立的通訊網就是這些城市 之間成本最低的通訊網。其中如果有相同權值的邊線時，MST 並非唯一 ; 如邊線的權值均不同，則 MST 唯一。


## 程式碼學習歷程： 

    這次的作業最重要的是要先知道Dijkstra 和 Kruskal 分別的步驟跟概念，Dijkstra是找到起點之後，試著把整張圖走完，到各個點最小cost ; 而Kruskal呢，則是另一面向，要怎麼用最少cost讓所有的點都被連到。以作業圖來舉例，0可以連到 1 或 7  8 可以連到 2  6 7  可能有不只一條連線，我能不能只留下必要的就好，也就是假設我得搭橋讓這9個點彼此之間能夠互相往來，我該怎麼搭 成本可以最低，要解的問題是這個。
    
    這次我一開始在寫了Dijkstra之後試跑測資的時候，出來的最小路徑數字跟助教給的不一樣。結果發現是我在找最小的時候沒有過濾掉已經不用找的部分，也就是if cand_path[node_pair] < shortest_val 這一行，改成 if cand_path[node_pair] < shortest_val and node_pair[1] not in shortest_dict.keys():，已經不用找的部分就是當目標點已經被加在shortest_dict裡面的時候，這樣的路徑就不用再加進candidate當中。 以作業圖來舉例的話 2 這個點 可以走 0 1 2 也可以走 0 7 8 2，這時候 後面的可能會蓋掉前面的 讓最小數字不再是最小，就會出錯。
    
        另外這次比較有趣的事是在寫kruskal時，繼上次我把BFS跟DFS的概念想做生活中的購物例子後，我真的覺得把一個抽象的概念換作實體的例子時，對我來說真的好理解很多，所以我在理解了Kruskal的流程之後，我發現其實可以把每個點視作各個“小島”，然後把所有可以蓋的橋按價錢由小到大排好，接著再把它一座一座建起來，當兩個島之間建好橋後就可以視為一個聯盟。 轉一個想法之後其實再轉成程式碼時，就比較容易理解，寫起來也很有成就感！：）
        
        這次的作業我在除錯的過程中，還有自己再把概念轉成比較實際的例子再去寫成程式碼，真的學到超多，也應證了老師上課說的寫程式本身就是在訓練及學習解決生活中所遇到的困難的一種能力，更是一種藝術，自己想要怎麼發揮就去下手～☺❤️
    


```python

```
