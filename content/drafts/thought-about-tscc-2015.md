Title: Thought about TSCC 2015
Slug: thought-about-tscc-2015
Date: 2015-05-02 16:10:17
Authors: m157q
Category: Thoughts
Tags: Thought, TSCC, HPC
Summary: Thought about the Taiwan Student Cluster Competition 2015
Status: draft

http://event.nchc.org.tw/2015/tscc/

TSCC (Taiwan Student Cluster Competition) 由台灣國家高速網路中心（簡稱國網中心）舉辦的台灣全國學生叢集電腦競賽，限高中生與大學生參加（研究生不可參加，但可擔任教練）。

以前都只有耳聞這個比賽，但沒參加，大學最後一年，因為一些緣分，和高中社團認識的一些人組成了一支橫跨中央、交大、中教大、竹教大的四校聯隊，不知道是不是這比賽第一支聯隊，因為這比賽通常是以校為單位組隊，主要原因是因為高效運算需要的設備成本對學生來說並不便宜，以校為單位的隊伍比較容易向學校申請一些相關經費，為校爭光等等之類的。而清大在這比賽一直是衛冕者，主要是因為他們在這方面真的投入蠻多心力的。

因為以前沒碰過高效運算、平行運算或是叢集運算這方面的東西，想說藉著比賽讓自己學習也未嘗不是件好事，但沒碰過就比較辛苦一點，一堆專有名詞都不太懂，只好寫下來紀錄一下。

2015 的決賽內容:

1.LAMMPS

LAMMPS主要是由美國能源部Sandia National Laboratories所開發之GNU開放軟體(open source)，它是一個以古典分子動力學為主的模擬應用程式，並附有蒙地卡羅、耗散粒子動力學等模擬方法，可模擬包含液態、氣態、固態、膠質等不同物質之結構、動力學、力學、…等微觀材料物性質之軟體，尺度可模擬數百至數十億顆原子。LAMMPS更支援個人電腦、大型平行運算主機、或GPU顯卡等設施執行運算，編譯之程式為C + +，並支持MPI、OpenMP與CUDA程式。並且是一個被設計成易於修改或擴展新的原始碼，因此可讓使用者免費使用或修改。

LAMMPS網址為: http://lammps.sandia.gov/

2.Einstein toolkit

Einstein toolkit為一求解初值邊界問題的開源科學模擬程式。主要應用在強重力場下的極端天文物理研究，如黑洞的形成及演化、中子星與黑洞碰撞、重力波計算等其他廣義的相對論磁流體系統，以提供未來重力波相關天文觀測所需要的理論模型。Einstein toolkit 基於Cactus 的插件式設計，支援MPI、OpenMP 以及向量擴展指令集，提供一般模擬過程所需要的元件，如高階有限差分、顯式時間演化積分、結構化自適應網格(structured adaptive mesh refinement)等，而研究者可著重在科學插件的撰寫與組合，控制模擬流程，充分發揮高速計算主機效能。目前主要的開發者為美國、德國、與加拿大的數值相對論研究群。

Einstein toolkit : http://einsteintoolkit.org/  
Cactus Framework : http://cactuscode.org/


3.多核心高效能程式調教

隨著多核心系統日益普遍，無論桌上型電腦、筆記型電腦甚至平板電腦或智慧型手機皆採用多核心處理器。如何充分使用多核心處理器所帶來的效能優勢進行工程科學計算，成為研究人員重要的課題。

多核心高效能程式調教試題將以工程科學計算作為案例提供Serial程式，參賽隊伍將可依計算環境、演算法特性等，透過平行程式語言(如：OpenMP、MPI、CUDA、OpenCL等)在競賽中所架設之環境進行平行效能測試。

希望參賽者利用對題目的了解、分析平行效率的瓶頸與瞭解平行程式撰寫，調整平行計算環境的設定，進而發揮最佳的平行計算效能；藉此增加對高速計算軟硬體環境之經驗。


