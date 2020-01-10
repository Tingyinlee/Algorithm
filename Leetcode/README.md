# :dart:LeetCode Practice:
---

## 155. Min Stack
Stack是具有「Last-In-First-Out」的資料結構(可以想像成一種裝資料的容器)，「最晚進入Stack」的資料會「最先被取出」，「最早進入Stack」的資料則「最晚被取出」。  
一般的Stack，會有以下幾個處理資料結構的功能：  
Push(data)：把資料放進Stack。把書放進箱子。  
Pop：把「最上面」的資料從Stack中移除。把位於箱子「最上面」的書拿出來。  
Top：回傳「最上面」的資料，不影響資料結構本身。確認目前位於箱子「最上面」的是哪本書。  
IsEmpty：確認Stack裡是否有資料，不影響資料結構本身。確認箱子裡面有沒有書。  
getSize：回傳Stack裡的資料個數，不影響資料結構本身。記錄目前箱子已經裝了多少本書。  
Queue是具有「First-In-First-Out」的資料結構，如同排隊買車票的隊伍即可視為Queue，先進入隊伍的人，可以優先離開隊伍，走向售票窗口買票，而後到的人，就需要等隊伍前面的人都買完票後才能買。  
一般的Queue，會有以下幾個處理資料結構的功能，配合圖二：
Push(data)：把資料從Queue的「後面」放進Queue，並更新成新的back。在Queue中新增資料又稱為enqueue。  
Pop：把front所指向的資料從Queue中移除，並更新front。從Queue刪除資料又稱為dequeue。  
getFront：回傳front所指向的資料。  
getBack：回傳back所指向的資料。  
IsEmpty：確認Queue裡是否有資料。  
getSize：回傳Queue裡的資料個數。  

---
## 705. Design Hash Set
1. 建立 Hash Table 並決定其長度。
2. 新增數值型態資料進入 Hash Table 中，決定資料再Hash Table中index的位置，key = index。若發生 Collision 的情況，很可能有多個 Key被分在Hash Table 中同一個 index ，此時就可以利用 Chaining 的方法， 使用 Linked list 把被分在 Hash Table 中同一個 index 的 Key 值串起來。  

> - Add : 先利用 Hash Function 取得 Table 的 index ，接著再利用 addAtTail每個資料依序串起來。  
> - Contains: 先利用 Hash Function 取得 Table 的 index ，接著再利用 Search 找到欲查找的資料。  
> - Remove: 先利用 Hash Function 取得 Table的 index ，接著再 利用 Delete 刪除欲刪除的資料。  

---
## 707. Design Linked List
Linked list(鏈結串列)是一種常見的資料結構，其使用node(節點)來記錄、表示、儲存資料(data)，並利用每個node中的pointer指向下一個node，藉此將多個node串連起來，形成Linked list，並以NULL來代表Linked list的終點。  
Linked List 是由「節點」(Node)組成的有序串列集合，節點又稱串列節點(List Node)。每一個節點至少包含一個「資料欄」(Data Field)和「鏈結欄」(Linked Field)。  
鏈結串列加入或刪除一個節點非常方便，不需要大幅搬動資料，只要改變鏈結的指標即可。


---
## 1290. Convert Binary Number in a Linked List to Integer
Hint1是說，轉成string或是array，再一一轉成int。
Hint2說可以使用bit operation。

這題相對簡單些，是比較概念類的題型，要對位元和邏輯運算子熟悉。
