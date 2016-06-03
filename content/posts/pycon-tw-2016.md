Title: PyCon TW 2016  
Slug: pycon-tw-2016  
Date: 2016-06-03 21:21:52  
Authors: m157q  
Category: Note  
Tags: Python, Conf, PyCon, PyConTW  
Summary: Just a note for PyCon TW 2016  
  
  
Really appreciate [eldarion](http://eldarion.com/) gave me the free sponsored ticket or I could not attend this biggest annual Python event in Taiwan.  
  
+ [官網](https://tw.pycon.org/2016/)  
+ [官方共筆](https://hackfoldr.org/pycontw2016)  
+ [官方聊天室](https://gitter.im/pycontw/2016)  
+ [直播頻道](https://www.youtube.com/channel/UCHLnNgRnfGYDzPCCH8qGbQw)  
  
---  
  
# Day 1 (2016/06/03 Fri)  
  
---  
  
## Keynote: The world after tomorrow by au（唐鳳）  
  
+ 與 Python 第一次接觸：2003 年，在台灣，Perl, Python, PHP 三個沒有大公司支撐的語言辦了個 Conf，沒想到反應熱烈，成為 OSDC.tw 的前身，直到 2014 年 OSDC 停辦。  
+ Perl 5：很多設計都是從 Python 的 pep 抄來  
+ 用 Open Source 參與公民社會：318, g0v  
+ 報導者：開源媒體  
  
---  
  
## R2: Strategies for concurrency and parallelism in Python by 洪鈺庭  
  
+ Synchronous Model  
    + 一次執行一個 task  
    + 最常用，最簡單，最直覺  
    + Demo  
        + `voice.RSS.TexttoSpeechAPI`  
    + 並沒有用到 concurrency 的概念  
+ Multi-threading  
    + 不一樣的 thread 可以 share 同一個 memory space  
    + create 一個 queue 再從 queue 拿出來  
+ GIL in Python  
    + 同一個時間只會讓一個 thread 執行  
    + 因為有些 Lib 不是 thread safe，所以直接做限制  
    + 不是所有 Python 的實作都有 GIL, CPython 有，但像 Jython 和 IronPython 就沒有。  
    + 既然一次只能執行一個 thread, 為什麼還是比 Synchronous 快呢？  
        + 因為剛剛的例子是 IO bound, 在等待的時間就可以 switch 到其他 thread 做事情。  
        + 如果是 CPU bound 的話，multithread 就沒啥太大的優勢，得用 multiprocessing  
+ Multi-processing  
    + 建一個 Pool, 然後用 subprocess 去處理事情。  
    + 對於過於龐大的程式的話，可能會造成 memory over-head.  
+ Distributed Workers  
    + 把 thread 抽出來，放到另外一個 machine 執行  
    + RQ (Redis Queue)  
        + A simple Python library backed by Redis for queueing.  
    + scalibility 會比較好  
+  Distributed Workers with Cloud Platform Service  
    + Iaas  
        + 自訂性比較高，但管理上會比較麻煩一點。  
    + Paas  
        + Instances 的增減 (auto-scaling) 都交由 cloud platform provider 管理，不用自己管。  
  
> Q&A 一堆人電講者是怎樣 LOL  
  
---  
  
## R2: Robot Framework: An ATDD Framework by Apua  
  
+ ATDD (Acceptance-test-driven development)  
+ Robot Framework 可以做到分散式測試，不只是個 automation tool  
+ Acceptance Test  
    + Minimal Accpetance Test  
        + 只取最小的集合，驗證這個產品是他想要的。  
    + End-to-End Acceptance Test  
        + 把所有能夠想到的測試都跑過一遍。  
    + 把一個很大的 User story 拆解成各種小的 test  
    + Behavior driven testing  
        + keywords: Given, When, Then  
        + keywords 其實就是 function  
        + robot framework 可以讓你用 @keyword 來將關鍵字綁定到特定的 function  
    + PyBot  
        + 可以把 keyword 的 traceback show 給你看  
        + 可以把所有 test cases 都直接 show 出來  
+ Flow  
+ Robot framework 的特性  
    + Format  
        + 支援各種常用格式  
    + Programmability  
        + Limited flow control  
            + 只有 for loop，沒有 while  
            + 只能用 ternary operator, 沒有 if else  
            + 透過嚴格的限制，讓你很難把 test cases 寫的很亂  
        + 支援把檔案當成是變數  
    + Hierechical structure  
        + Variable files in YAML, Python  
        + Resource files to collect keywords and libraries  
        + File and directory to organize setup/teardown  
    + Tagging  
        + Category to select  
        + Set critical cases  
            + 可以很容易做到 small test  
        + 可以自己訂 tag 來做到不同的不同的版本使用不同的測試環境和測資，跟上面的 variable files 做結合。  
    + Documentation  
        + 支援把 test case 以 docstring 的方式撰寫，讓可維護性提高  
    + Remote Library  
        + 遇到把跑測試的環境和測資是分開時，這很好用。  
        + 使用 XML-RPC protocol  
    + 其他  
        + 可以客製化 report  
        + IDE support  
        + 支援自建 keywords  
        + 有支援使用 API 操作  
        + CI Plugin  
            + Jenkins  
        + Third party plugins on pip 也很多  
+ Summary  
    + Robot Framework 提供了很方便的方式讓你可以很快針對需求去撰寫測試。  
    + ATDD breakdown story  
        + Acceptance test  
        + Implement/reuse keyword  
        + Automation for testing  
    + 2015/12/31 開始支援 Python 3  
+ Q&A  
    + Parallel PyBot  
        + 這不確定有沒有疑慮，因為 test cases 最好是循序跑比較好，因為有些可能會有相依性。  
  
>  Q&A 好熱烈，看來很多人對 testings 都有蠻多疑問和蠻有興趣的。  
  
---  
  
## Keynote: Python 導入系統軟體教學 by Jserv  
  
+ 20 多年前臺灣走在軟體產業的前端，從辦公軟體到作業系統，沒有什麼是臺灣沒辦法寫的，開源軟體貢獻度大勝亞洲各國；20 多年後，在頂大的創新競賽上，評審教授會跟你說「為什麼不用 ApplePay 就好。」  
+ 20 年前台灣許多軟體都有人開發，除了作業系統和編譯器沒有以外。  
+ 15 年前台灣對 Linux 和 BSD 的貢獻是領先亞洲其他國家的。  
+ 蕭柏納說：「生命不該是支燃燒的蠟燭，燒完就沒。而是一把火炬，應該要努力發光發熱，然後交到下一代的手上。」  
+ Nand2Tetris  
+ ARRC 前瞻火箭計劃  
+ 帶學生參與真正的開源計劃，由於貿然投入大型開源計劃的難度是很高的，所以從自己打造比小型但是完整開源系統帶學生做起。然後積極投稿世界一流的 Open Source Conference，讓學生可以被國際看見外，也能夠獲得成就感，並繼續投入到開源的世界中。  
+ 學生是有熱情的，參與 Open Source 的人也比以前多，但大多數人都是自己玩自己的，學生不知道如何跟人家打群架。  
  
---  
  
## R1: From Pandas to GeoPandas by 尼斯  
  
+ GeoPandas == Pandas + GIS  
+ 台灣常用的座標參考系統  
    + WGS84 (Lat/Lon)  
    + TWD67 (TM2)  
    + TWD97 (TM2)  
+ Shapdefile 的結構  
    + .dbf  
    + .shp  
        + 空間的形狀、位置  
    + .shx  
        + 索引  
    + .prj  
        + 投影資訊  
+ Import the GeoPandas  
    + 結合數值資料並做視覺化  
    + 為了要 join 兩種資料，必須要做些預處理。（例如：欄位具有資訊，但格式不符合）  
    + 用 groupby 把某一欄位有相同值的資料排好再使用 aggergation function 將這些資料合併在一起  
    + 製作區域密度圖  
+ 情境：忠孝橋引道拆除，要賠償施工範圍半徑 500 公尺內影響到的里的所有里民  
    + 疊圖分析 (intersection)  
        + 簡單來說就是把要的資料拿出來，然後取交集，找出目標區域。  
+ 補充（都可在 Jupyter Notebook 進行）  
    + Spatial join  
        + 根據空間的關係去做 join  
        + 分析住商資料台北市各個里的平均地價  
    + Folium  
        + 轉成 GeoJson 後，透過 Folium 顯示出來。  
+ Q&A  
    + Open Data 還不夠完善，有時候可以從 Open Street Map 拿到資料。  
    + 目前只能做 2D 的分析，沒辦法做到 3D 的分析。  
  
---  
  
## R0: 大型互動展覽的 Python 應用 by 陳炯廷  
  
> RPi3 上跑 Django 只 run 一支 scanner.py ?  
  
+ Rough Prototype => Auto Update => More Development  
    + 開機時執行 Auto Update  
+ 為什麼要用 Django?  
    + 有 Admin 介面，不熟悉 Linux 的人也可以進入設定 server 佈署  
+ 加上一個簡易的 HeartBeat 就可以有個簡易的後台  
+ 原本預計用 Zeroconf + Avahi 自己找主機，但因為不同的 team 屬於不同的 subnet 而作罷。  
+ 掃 QR Code 來設定機器  
+ 全區開機卡  
    + pip install wakeonlan  
+ 全區關機卡  
    + 收到特定的 UDP 封包就會關機  
+ Redis PubSub  
    + redis-py  
+ 透過 socket.io-emmitter 這個 Python 套件可以用 Python 跟 socket.io 做溝通  
    + 但這個套件好像沒在 maintain 了，可能要多花時間嘗試一下。  
+ Django  
    + 用 django-rest-framework 做簡易的 API 設定  
    + 用 django-allauth 做手機登入  
+ 文件用 Sphinx 產生，但總共有四間不同的公司需要 access  
    + 後來直接把頁面放在 Django 底下，但透過加上 `X-Acce-Redirect` Header 讓 file 給 Nginx host，減輕 server 的負擔。  
+ 不要以為把資料丟到 Cloud Platform，就不會有斷線的問題。因為這個才改成比較複雜的架構，但可以在聯外網路斷掉的時候正常運作。  
+ 展場的供電通常在閉館會斷電，除非有特別要求要 24 小時供電。  
+ 展場的電腦常放在很難碰到的地方。  
+ [Pure Data](https://puredata.info/) 很難串接 HTTP API，連 parse JSON 都很困難，只好弄一個簡單的 HTTP protocol 來溝通。  
+ 展場的實體東西只有一座，開展了就是 production，沒辦法分 dev / staging。  
  
---  
  
## R0: Boost Maintainbility by Mosky  
  
+ [Making wrong code look wrong - Joel on software](http://www.joelonsoftware.com/articles/Wrong.html)  
+ Maintainbility  
    + Definition: To understand a random line, the lines you need to read back.  
+ 現在拿錢砸下去就有一堆機器可用，但拿錢砸學校無法生出一堆 programmer，好的維護性才能夠節省時間。  
  
### Making it zero  
  
+ "Be exact & consistent."  
    + 精確的命名變數，不要用些模稜良可的名字。  
    + 要保持一致性，和英文的慣用法有關。  
  
### 範例  
  
`result = ...` => (X) #不知道是什麼的 result  
`parsed_dict = ...` => (O)  
  
用動詞開頭代表 function  
用形容詞、介系詞或句子來代表 boolean 值  
  
#### Ops Hinit  
  
##### for non-callable  
+ `_no`: numeric  
+ `_<abstract type>`:  
    + `_seq`: for sequence  
    + `_gen`: for generator  
  
##### for Callable  
    + `<verb>_`  
    + `<yes-no question>`  
    + `to_<thing>`  
  
#### explicit unknown  
    + `_x`: anything  
        + rather tahn an ambiguous name.  
        + You won't forget to determine the ops it supports.  
        + Use hasattr or isinstnace later.  
##### So, avoid None  
```  
user = query_user(uid)  
user.is_valid()  
  
# Then `query_user` returns `None` => BOOM! An `AttributeError`!  
# Accept Excetion?  
#   Y: just raises it  
#   N: use a dummy object like ''  
```  
  
##### 不夠精確的例子  
  
`arg = parse(arg)` => (X)  
`arg_d = parse(arg_json)` => (O)  
  
  
##### str/x  
+ `_key`: key (of a dict)  
+ `_url`: URL  
    + percent-encode  
+ `_json`: JSON  
    + `json = json.loads(json)` => (X)  
    + JSON is a string  
+ `_html`: HTML  
    + avoid XSS  
+ `_sql`: SQL  
    + avoid SQL injection  
  
  
##### numeric/x  
  
+ `_no`: number, #  
+ `_idx`: index  
    + `>= 0`  
    + or just `i`, `j`, `k`  
+ `_secs`  
    + It's seconds  
+ `_pct`: percent  
    + `n = 10%`  
    + `n_pct = 10`  
  
  
#### Structure Hint  
  
##### users  
  
```  
users = {  
    'a': 'a@a.com',  
}  
```  
(X)  
=>  
```  
uid_email_map = {  
    'a': 'a@a.com',  
}  
```  
(O)  
  
  
##### for dict & tuple  
  
+ `<key>_<value>_map`  
+ tuple  
    + `_pair`  
    + `_pairs`  
        + 2-level-tuple  
    + `<1st>_<2nd>_<3rd>_triple`  
  
##### Don't use me  
  
+ `_<name>`  
+ Don't use when out of  
    + a module  
    + a class  
  
  
#### Performance Hint  
  
##### Should I cache it?  
  
+ `get_`: memory op  
+ `parse_` / `calc_`: CPU-bound op  
+ `query_`: IO-bound op  
+ `query_or_get_`: IO-bound op with cache  
  
  
### Progressive From Zero  
+ 可以用縮寫，但不要自己發明縮寫。  
+ Define in comment  
    + 用註解說明這個簡寫的全名是什麼  
    + `# TODO: ...`  
    > 拜託不要用 `# TODO` 啊...  
    > 最近被這荼毒的好慘，  
    > 有 version control 跟 issue tracker 就不應該這樣用啊，  
    > 留了一堆過沒多久搞不好自己都忘記。  
    > 這我記得在 《Clean Code》 裡頭就有說過啦，  
    > 除非真的完全沒用 version control 跟 issue tracker 可以紀錄，  
    > 否則這些東西應該要寫在 commit log 裏面，  
    > 然後開個 issue 來詳細描述 TODO 啊。  
+ Paragraph & Section  
    + 適當的使用空白行，不要全部都擠在一起。  
    + Title Comment: 當一個 function 做的事太多導致太長難以閱讀的話  
+ Line Functions Up  
    + 讓 trace back 函數時候的方向是一致的  
    + 有助於模組化  
  
### Face Bad Smell  
+ Comment  
    + pitfalls: the actual return type, side effects  
+ Seal it with better name or stabler wrapper  
+ Stay focused  
  
> 老實說這樣的命名法讓我彷彿看見匈牙利命名法的影子，  
> 但的確這樣命名起來會省了很多麻煩，  
> 總之就是一致性，  
> 公司的話就需要 Coding Style 相關的規範去要求大家共同遵守了。  
> (然後我好像聽見靜態語言的嘲笑聲）  
  
---  
  
# Day 2 (2016/06/04 Sat)  
  
---  
  
# Day 3 (2016/06/05 Sun)  
