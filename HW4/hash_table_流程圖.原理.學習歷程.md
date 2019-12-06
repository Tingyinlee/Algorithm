
了解Hash流程圖及原理的參考資料：
1. 演算法圖鑑 by石田保輝 ＆ 宮崎修一
2. Hash Table原理參考：https://zh.wikipedia.org/wiki/哈希表
3. Hash Function原理參考：https://en.wikipedia.org/wiki/Hash_function
4. 老師上課的PPT參考內容：

    a. https://docs.google.com/presentation/d/e/2PACX-1vT1HO9Nl475k2bR0l1x8_Tr4V5Wzx0BEqp9bpmHckvj8kTeJehhYVlOJUDVPhLQm6kjGCJ_sLMSBUw5/pub?start=false&loop=false&delayms=3000&slide=id.p

    b. https://kite.com/python/examples/2084/crypto-generate-a-new-md5-hash

# Hash table 流程圖：


```python
![] (https://raw.githubusercontent.com/Tingyinlee/Algorithm/master/Pictures/1.jpg)
![] (https://raw.githubusercontent.com/Tingyinlee/Algorithm/master/Pictures/2.jpg)
![] (https://raw.githubusercontent.com/Tingyinlee/Algorithm/master/Pictures/3.jpg)
```

# Hash table 雜湊表原理：

##### Hash table（雜湊表），是根據鍵（Key）而直接查詢在內存存儲位置並儲存成對數據的資料結構。也就是說，它通過計算一個關於鍵值的函數，將所需查詢的數據映射到表中一個位置來查詢記錄，這加快了查找速度。這個映射函數稱做雜湊函數，存放記錄的數組稱做雜湊表。

> For Example:
為了查找電話簿中某人的號碼，可以創建一個按照人名首字母順序排列的表（即建立人名x到首字母F(x)的一個函數關係），在首字母為W的表中查找「王」姓的電話號碼，顯然比直接查找就要快得多。這裡使用人名作為關鍵字，「取首字母」是這個例子中雜湊函數的函數法則F( )，存放首字母的表對應雜湊表。

# Hash function 雜湊函數原理：

##### 雜湊函式（英語：Hash function）又稱雜湊演算法，是一種從任何一種資料中建立小的數字「指紋」的方法。雜湊函式把訊息或資料壓縮成摘要，使得資料量變小，將資料的格式固定下來。該函式將資料打亂混合，重新建立一個叫做雜湊值（hash values，hash codes，hash sums，或hashes）的指紋。雜湊值通常用一個短的隨機字母和數字組成的字串來代表。好的雜湊函式在輸入域中很少出現雜湊衝突。在雜湊表和資料處理中，不抑制衝突來區別資料，會使得資料庫記錄更難找到。

>  ### *Hash function特性： 
1. 輸出的雜湊碼數據**長度不變**。
2. 輸入相同的值必定會產生相同的輸出。
3. 即使輸入的數據很相似，只要有一個位元的差異，輸出值就會相差甚遠。
4. 輸入**完全不同**的數據時，即使機率很低，仍可能產生相同的雜湊碼。 這稱為「hash collision」。
5. 從雜湊碼倒推出原始數據是**不可能**的。數據的輸入和輸出均為單一方向，這點和「加密」大相徑庭。
6. 用以決定雜湊碼的計算過程比較簡單。

> ### 補充：
Hash function 的演算法有數種，代表性的演算法包括MD5, SHA-1, 以及SHA-2...等。

# 學習歷程： 

這次的作業聽老師說相比之前的很簡單，一開始還很開心，結果我實際開始做之後整整花了七個多小時，覺得雖然是有用到Linked-List的概念，但是我覺得這次的對我來說反而更複雜了一些，因為多加了array的概念之後，再打程式碼時，我就開始感到蠻混亂的。但Hash Table的概念是比較好理解的，就是轉成程式碼時會一直卡住，尤其是在最難寫的remove的部分，我也是卡了很久，因為要考慮的地方比較多，又在想要怎麼一次把有重複要刪的目標刪光，結果我最後的解決辦法是，先處理掉頭，再來處理從第二個開始之後也要刪的。整體來說，我寫出的順序是，先按照老師在ＰＰＴ上付給我們的表，把16進位數字轉成10進位，接著先寫出add的function接著是contains，最後再寫remove的部分。 最後再用助教給我們參考的測資測試我的程式碼有沒有錯誤～(一開始第一次測的時候pig應該要被remove的部分還是顯示了TRUE，所以我又花了很長一段時間去debug...)，但還不錯，最後有找到迴圈沒寫好的地方，重新修正後測資總算是通過了，在這次的debug中也學到了不少！：）
 ***
 在這週二老師給我們在可堂上體驗pair programming的過程，我真的覺得很不錯，過程中我喜歡當駕駛大過於當導航的，因為我覺得自己還無法夠格當一個負責導航的ＸＤ 我功課寫的Hash是運用linked list的「概念」，重新寫了一份hash的(不是運用呼叫linked list)，但在星期二的課堂上，我跟我的pair programming的對象，先是由他負責導航，寫出了一份「半新」的hash(是結合並利用我過去寫過的linked list）～ 
 
雖然說是寫一樣的東西，但我卻覺得意外(好玩XD)有學習成效，經過這次的體驗，我覺得學到很多！不僅讓我心認識到一位很厲害的(也是外系)的同學，讓我可以吸收別人的想法，並一起切磋出新的東西，還可以一邊一起學習跟進步，這是在演算法課上蠻特別的一次經驗！


```python

```
