Title: 我的新鮮人面試紀錄  
Slug: first-job-interviews  
Date: 2016-02-02 23:47:37  
Authors: m157q  
Category: Life  
Tags: interview, resume, job  
Summary: 紀錄我人生第一次找工作的面試過程  
  
  
## 前言  
  
從去年 11/13 開始寫完我的 LinkedIn profile 後，算是開始找工作的起點。  
但過沒多久就發現，LinkedIn 充其量只能當作參考，也不是必要的，最重要的還是 resume。  
  
  
### LinkedIn 好難用，所以寫了個程式。  
  
當時因為覺得 LinkedIn 很難用，  
再加上花了不少時間寫 LinkedIn profile，懶的重寫一份 resume。  
於是異想天開的寫了一個把 LinkedIn profile 轉成 markdown format 的工具:  
[linkedin2md](https://github.com/M157q/linkedin2md)  
這樣我就可以偷懶直接用 LinkedIn 生一份 resume 出來。  
  
  
### 公司要的是 Resume，不是 CV。  
  
結果當然是個悲劇，  
因為 LinkedIn 上的形式比較像是 CV，紀錄你所有做過的事，  
這對一份 resume 來說實在是太過於雜亂無章且毫無重點可言，  
雖然跟我的經歷也有點關係就是，  
因為一直就是有興趣的東西我就會去碰，所以容易給人一種鼯鼠五技而窮的感覺。  
  
  
### 覺得整理想去的公司好麻煩，乾脆整理在 GitHub 上  
  
於是過了一個月，到了十二月中旬，  
才把[第一版英文履歷](https://github.com/M157q/find-jobs/blob/master/archives/version-1/resume.pdf)生了出來。  
之後大概就是往 Web Backend 跟 DevOps 這兩個職位去找，  
並把想投的公司及狀況紀錄在 [Issues · M157q/find-jobs · GitHub](https://github.com/M157q/find-jobs/issues)。  
  
  
### 透過獵人頭找工作  
  
然後又想到之前參加某個 Open Source 的 conf 時，  
看到臺灣有家叫 [sudo](https://sudo.com.tw) 的新公司，  
專門在幫軟體工程師找工作，  
基本上就是獵人頭這樣。  
於是就到他們網站上用 GitHub 帳號登入，  
把相關資料填一填跟履歷上傳後，  
申請該平台上面的職缺。  
（必須說這平台比 LinkedIn 簡單好用多了，雖然因為是新平台還有蠻多 bug 就是，  
但我有反應的 bug 跟意見他們的工作人員都還蠻快就回覆然後請工程師解決。  
而且 sudo 上的履歷支援 markdown 語法，光是這點我就覺得比 LinkedIn 好用了。  
我一直覺得 LinkedIn 自訂的 description 不能用超連結，只能用純文字 URL 是件很扯的事。）  
  
  
### 履歷寫的太爛，被慘電。  
  
之後在去年十二月底收到第一個面試通知，  
期間也一直在修改我的履歷，  
尤其是在收到第一個面試通知之前，  
跑去成大當面給 Jserv review 我的第一份 resume 被慘電 3 個小時，  
著實獲益良多。  
詳細內容則紀錄在 [程式設計師的履歷撰寫要點](/posts/2016/01/22/how-to-write-a-resume-for-programming-jobs/)  
  
---  
  
## 面試紀錄  
  
### Tagtoo - 塔圖科技  
  
+ 應徵職位：Web Backend (Python) Engineer （透過 sudo 投遞）  
    + <https://github.com/M157q/find-jobs/issues/10>  
+ 面試時間：2015/12/30 16:00  
+ 面試地點：台北市光復南路612號5樓  
+ 面試官：Teddy (CEO)  
+ 面試過程  
    + Teddy 跟我介紹 Tagtoo 的 Server 架構，說明公司內部會需要用到哪些東西，主要就網站後端用 Python, 前端基本的 JavaScript, HTML, CSS 可能會需要支援，但主要是後端開發。然後 CI 用 Travis, CD 用 Google Cloud Platform。大致介紹完後跟我說明 2016 年的目標是進軍東南亞的廣告市場，因為台灣的市場開發的差不多了，所以會有新的挑戰可以做。過程中都可以隨時提問，我對 server 的架構問了些問題。  
    + 之後問了我的兵役狀況，就把從常備役變免役的事敘述一遍。然後又問我為什麼沒繼續唸碩士，就把我看到很多學長姊進了 Lab 也沒辦法做自己有興趣的 Project，大部份都是接 Lab 裡的學長姊留下來的論文計劃，或是教授新接的計劃，甚至有些人連為什麼要唸碩士都沒有個明確的目標，就覺得大家都繼續唸上去，就跟著申請跟考試，有了就去唸，當然也有人是因為不想當兵想當研發替代役而唸。我坦白說我現階段對於唸碩士沒有什麼強烈的動機和意願，想先出來工作瞭解業界的情況和會用到的東西，再來看需要學什麼理論，一邊準備托福，之後考慮到美國發展。  
    + 然後提到了履歷，Teddy 說有先看過我的 GitHub (這點讓我當下小開心了一下) ，然後問我的履歷中印象最深刻及收穫最多的是哪一項，並描述這項事情的內容。我就選了大學時弄的專題，把專題的架構以及各個部份是在負責什麼功能，以及大致上是如何去實作的過程都講了。得到的回應是覺得我還不錯，因為面試過許多工程師都無法清楚描述自己做過的專案。  
    + 被問到「在做過的事情中，跟專業技能無關的部份遇到的最大困難是什麼？」。就提了大學專題在做上台報告的時候，因為做的東西是比較偏分析類，不像其他組有的做遊戲、有的做嵌入式等等，有成品可以 Demo，所以我這組在報告的時候就顯得頗枯燥乏味，於是深深體會到將專業技術清楚得表達是很重要的一件事。  
+ 結果  
    + Offer Got  
    + 60 K * 13  
  
  
### 17 Media (就做 17 App 的那家)  
  
+ 應徵職位：API Backend Developer / Cloud System Admin （透過 sudo 投遞）  
+ 面試時間：2016/01/08 11:30  
+ 面試地點：台北市信義區信義路五段 2 號 6 F (震旦大樓)  
+ 面試官：Popo (CEO)  
+ 面試過程  
    + 早到五分鐘，不過會議桌好像有人在談生意，所以我就在沙發上稍微等了一下，順便觀察公司環境。環境蠻寬敞明亮的，員工彼此都是坐在好幾張大桌子上，沒有隔版。有大冰箱、一整櫃零食櫃還有咖啡機，放著員工自己想聽的音樂，基本上就是我喜歡的那種新創環境。  
    + 一開始 Popo 要我自我介紹，我就照履歷上列出來的事情每件稍微講了一下，我邊講他才邊點開連結看，感覺應該沒有事先看過。  
    + 之後問了我對 Node.js 的熟悉程度，就跟他說大學專題的時候我有自己稍微寫一下，但沒有到很熟。之後聊一聊就說如果之後進去的話，應該就是負責撰寫 API doc 跟調整 Node.js 的部份。  
    + 之後大致上就是一些閒聊，我也記得不太熟了，就有問他對於 17 App 前陣子染黃有什麼看法和應對，聽到一個我覺得還蠻有趣的答案。在新聞大幅報導過後，他們現在對於色情是完全禁止的，檢查的方法是透過程式定時去擷取實況用戶的畫面，再丟給 Machine Learning 去判斷是否有色情的成份，如果有的話會先暫時停止播放，再經由人工確認，如果確定是色情的話就會直接 ban 掉帳號。  
    + 然後聊一聊，聊到程序員鼓勵師，還聊到學到了一個新單字，聖人模式的英文叫 "Moment of Clarity"，不要問我為什麼會聊到這個 www  
+ 結果  
    + 無聲卡  
  
  
### Akatsuki - 曉數碼  
  
#### 第一階段  
  
+ 應徵職位：Application Engineer / Backend Server Engineer （透過 sudo 投遞）  
+ 面試時間：2016/01/11 14:00  
+ 面試地點：松山區南京東路四段16號7樓B  
+ 面試官：Kana (HR Manager, Eng), ??? (HR, 中文)  
+ 面試過程  
+ 結果  
  
  
### VMFive  
  
+ 應徵職位：Cloud Engineer in Operation （透過 Referral）  
    + <https://github.com/M157q/find-jobs/issues/14>  
+ 面試時間：  
+ 面試地點：  
+ 面試官：  
+ 面試過程  
+ 結果  
  
### CHOCOLABS - 歐酷網路  
+ 應徵職位：Cloud Engineer in Operation （透過 Referral）  
    + <https://github.com/M157q/find-jobs/issues/14>  
+ 面試時間：  
+ 面試地點：  
+ 面試官：  
+ 面試過程  
+ 結果  
  
---  
  
## 心得  
  
