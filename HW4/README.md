## *Hash function特性： 
>1. 輸出的雜湊碼數據**長度不變**。
>2. 輸入相同的值必定會產生相同的輸出。
>3. 即使輸入的數據很相似，只要有一個位元的差異，輸出值就會相差甚遠。
>4. 輸入**完全不同**的數據時，即使機率很低，仍可能產生相同的雜湊碼。 這稱為「hash collision」。
>5. 從雜湊碼推出原始數據是**不可能**的。數據的輸入和輸出均為單一方向，這點和「加密」大相徑庭。
>6. 用以決定雜湊碼的計算過程比較簡單。

> ### 補充：
Hash function 的演算法有數種，代表性的演算法包括MD5, SHA-1, 以及SHA-2...等。

## Hash Table流程：
- 1.	建立Hash Table並決定其長度
 
- 2.	新增資料進入Hash Table
新增非數值型態資料「dog」進入Hash Table中。  
計算該資料須存放的位置: 以MD5編碼並將編碼結果轉成十進位，並將該數值除以Hash Table的長度求餘數。  
「dog」以MD5編碼並將編碼結果轉成十進位後為909720205502626453 5080901219663267845，除以Hash Table的長度求餘數為0。  
將「dog」存放至Hash Table的index=0的位置。  
   
新增非數值型態資料「pig」進入Hash Table中。  
「pig」 以MD5編碼並將編碼結果轉成十進位後為909720205502626 4535080901219663267845，除以Hash Table的長度求餘數為2。  
將「pig」存放至Hash Table的index=2的位置。  
   
新增非數值型態資料「cat」進入Hash Table中。  
「cat」 以MD5編碼並將編碼結果轉成十進位後為2771022202490735 55409885156483852860632，除以Hash Table的長度求餘數為2。  
將「cat」存放至Hash Table的index=2的位置。  
在index=2的位置發生Collision，利用Chaining的方法，使用Linked list將分在Hash Table中同一個index的資料串起來，將「cat」接在「pig」後面。  
   
- 3.	刪除Hash Table中資料
在Hash Table中刪除新增非數值型態資料「cat」。  
計算該資料須存放的位置: 以MD5編碼並將編碼結果轉成十進位，並將該數值除以Hash Table的長度求餘數。  
「cat」 以MD5編碼並將編碼結果轉成十進位後為2771022202490735 55409885156483852860632，除以Hash Table的長度求餘數為2。  
訪尋位於Hash Table 中index=2位置的Linkedlist，並刪除含有「cat」的node。  
  
- 4.	查找Hash Table中的資料
在Hash Table中查找非數值型態資料「cat」。  
計算該資料須存放的位置: 以MD5編碼並將編碼結果轉成十進位，並將該數值除以Hash Table的長度求餘數。  
「cat」 以MD5編碼並將編碼結果轉成十進位後為2771022202490735 55409885156483852860632，除以Hash Table的長度求餘數為2。  
訪尋位於Hash Table 中index=2位置的Linkedlist，並查找含有「cat」的node。如找到符合條件的node則返回 "cat" is in the hash table.。


