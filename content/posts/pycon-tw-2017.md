Title: PyCon TW 2017  
Slug: pycon-tw-2017  
Date: 2017-06-09 17:51:37  
Authors: m157q  
Category: Note  
Tags: Python, PyCon, PyCon TW  
Summary: Note for PyCon TW 2017 (2017/06/09 ~ 2017/06/11)  
  
  
Website: <https://tw.pycon.org/2017/en-us/>  
Portal: <https://tw.pycon.org/2017/en-us/portal/>  
Chat: <https://gitter.im/pycontw/2017>  
Collaborative Notes: <https://hackfoldr.org/pycontw2017/>  
Quiz Bot: <https://pycontw2017-quizbot.herokuapp.com/>  
  
  
---  
  
# Day 1 (2017/06/09)  
  
## Keynote: Choices for Smarter AI  
  
Speaker: 林軒田  
  
有點像是在大學上第 1 堂 AI 概論的感覺，  
前面 30 分鐘基本上沒有啥重點 XD。  
  
後面 30 分鐘開始講開始接觸 AI 會面臨哪些 Choices  
  
+ Motivation vs Feasibility  
    + Motivation  
        + something publishable? (maybe just for academia)  
        + something profitable?  
    + Feasibility  
        + Modeling  
        + Timeline  
        + Budget  
+ Big AI problems comes from Big Data  
    + generate from motivation  
        + variety: dream more in big data age  
        + velocity: evolving data, evolving problem  
    + generate from feasibility  
        + volume: computational bottleneck  
        + veracity: modeling with non-textbook data  
            + 資料的 noise 會比教科書上多很多  
    + tip  
        + often needing "choose and learn" towards good problems  
+ Human vs Machine-er Route  
    + Human  
    + Machine  
        + objective criterion  
        + use computing power  
        + continuous improvement  
+ How to measure AI goal  
    + "Computers are useless, they can only give you answers."  
    + Spec for Program  
        + tip: always start with reasonable, measurable & priortized goals for AI.  
+ What Data to (or not to) Use?  
    + Bring Your Own Bottle  
    + Design Your ...  
    + Choice factors for Data  
        + Utility  
        + Necessity  
        + Quality  
        + Cost  
        + tip: garbages (data) in, garbages (AI) out. Choose your data.  
    + More Data Construction  
        + 不用一開始就要 AI 做事情，最好先用自己的腦袋先做一些 Data Analysis，再讓 AI 幫你完成這些事  
+ What Model to Start?  
    + myth: 即便有大量的資料也不該從最複雜的模型開始  
    + Linear (Simpler) Model First  
        + Keep It Simple and Stupid  
+ What Improvements to take  
    + Overfitting  
        + 控制模型的複雜度、做些資料的清理與選擇，讓你的模型可以維持在能夠運作的程度  
    + Misfitting  
        + 要 AI 做的好，要確定它在學習的東西是跟你最後的目標有關係  
    + Over-reusing  
        + "If you torture the data long enough, it will confess"  
        + 當你過度重複處理你的資料，到最後的結果可能是會被汙染的，所以要儘量避免掉這件事。  
+ How to Verify and Deploy?  
    + Code Deployment Workflow  
        + Development => Staging => Production  
    + AI Deployment Workflow  
        + Offline => Online => Production  
            + Offline  
                + 在這個階段常常會跟 Online 的部份有 Misfitting 的問題，所以通常只是做正確的驗證  
            + Online  
                + 這時候的 criterion 會跟你的目標比較接近  
                + 要謹慎選擇跟誰比較，跟太爛的比會太過樂觀，跟太好的比可能會過度調整而產生 Overfitting。  
                + Human trust 會比你原本的目標來的重要，因為一個能用的 AI 是需要取的人的信任的，就算你達到目標，如果結果跑出來讓人不滿意的話，一樣達不到效果。要讓人能夠接受這個結果，才能夠發揮這個 AI 的價值。  
    + 跟你的選擇一起學習，時時刻刻要把限制考慮進去，這樣才能夠做出比較好的決策。  
    + 在訓練 AI 的時候，就像訓練神奇寶貝一樣，會遇到非常多的選擇，而這些選擇也都真的會影響到你訓練出來的 AI 的好壞  
+ Q&A  
    + 剛剛演講的內容涉及到 Data Engineer 和 Data Scientist 的部份，想請問這兩者的區別？  
        + > 硬要區分的話，Data Scientist 比較偏向設計，而 Data Engineer 比較偏向實作與驗證。但我自己是傾向不去區分，因為最終會需要的能力是跨領域的，所以都要瞭解才是比較好的  
    + 剛剛提到訓練出來的 AI 要取得人的信任，但這個常常會牽涉到客戶的利益，這該怎麼處理？  
        + 要確認彼此的期待是合理的  
  
## Python 開源軟體考古 - 以 Viper 為例  
  
+ Speaker: [陳坤裕 KunYu Chen](https://github.com/18z)  
+ GitHub repo of this talk: <https://github.com/18z/viper-research>  
+ Viper: <https://github.com/viper-framework/viper>  
+ Collaborative Note: <https://hackmd.io/s/H1yP4MQye#1050-1120-talk-python-開源軟體考古-以-viper-為例>  
  
覺得這場講的東西挺不錯的，  
都算是講者自己整理出來的心得，  
介紹了一些可以使用的工具，  
也講了他是怎麼去 trace 以及觀察了哪些東西，  
不失為一個拿來 trace open source project 的方法，  
可能可以幫助自己更容易對於 open source contirbute 做貢獻。  
  
可以產生 dependency graph 的工具：<http://furius.ca/snakefood/>  
  
  
## TenslorFlow Wide & Deep Data Classification the Easy Way  
  
Speaker: Yufeng Guo @yufengG  
Slides: <https://www.slideshare.net/YufengGuo4/pycon-tw-tensorflow-wide-deep-data-classification-the-easy-way>  
Code: <https://github.com/amygdala/tensorflow-workshop/tree/master/workshop_sections/wide_n_deep>  
  
  
## Keynote: The State of Python for Education  
  
+ Speaker: Carol Willing  
+ Collaborative Note: <https://hackfoldr.org/pycontw2017/https%253A%252F%252Fhackmd.io%252Fs%252FHk-NVGXke>  
  
for Education => X  
for Learning => O  
<https://github.com/jakevdp/WhirlwindTourOfPython>  
  
+ Learning with Python  
    + [JupyterNotebook](https://github.com/jupyter/notebook)  
    + [JupyterLab](https://github.com/jupyterlab/jupyterlab)  
    + [pyvideo](http://pyvideo.org/)  
+ Creating opportunities  
+ Scaling Globally  
+ Call to Action  
    + Join PSF and Python in Education  
    + Participate in a sprint  
    + Give a talk or write a post  
    + Offer a workshop  
    + Contribute to a favorite project  
        + Open an issue  
        + Fix typo  
        + Send pull request  
    + Share your creations  
  
  
## Building Microservices in Python 個案分享  
  
+ Speaker: Jonas Cheng  
+ Slides: <https://www.slideshare.net/jonascheng3/building-microservices-in-python-pycon2017>  
+ Collaborative Note: <https://hackmd.io/OwQwDCBMYEaQtADgJwBYT1WSj7IIwDMh8ApgCYCskyklMyi5qQA=?both#1455-1540-talk-building-microservices-in-python-個案分享>  
  
Soocii 是趨勢科技為了弄手機群聊而獨立出來的子公司  
  
跨服務間的溝通最好是一個 transaction 就結束，  
如果要額外呼叫其他的服務的話，  
最好採用 async 的方式，  
避免因為時間太長而被 timeout、影響 UX。  
  
  
## Python Module in Rust  
  
+ Speaker: 許邱翔 (dv)  
+ Slides: <https://docs.google.com/presentation/d/1mTw-4buKDTqPNzJS03s2I0apBMal-SaeKk1dHDSE6fk/pub?start=false&loop=false&delayms=3000&slide=id.g22c75fc6c3_0_6>  
+ Rust 的生態系  
    + 特性  
        + Memory safety without GC  
        + Compiled language  
        + Strong, static type  
        + 效能與 C / C++ 接近  
    + Tools  
        + Crates (Like PyPI in Python)  
        + Cargo (Like pip + setuptools)  
            + <http://doc.crates.io/>  
        + rustup (like pyenv)  
            + <https://www.rustup.rs/>  
        + RFCs (like PEP)  
            + <https://github.com/rust-lang/rfcs>  
+ How can Python play with binary  
    + ctypes  
    + CFFI  
        + PyPy 團隊的實作  
    + CPython Extension  
        + CPython 官方實作  
+ How can Python play with Python  
    + <https://github.com/dgrunwald/rust-cpython>  
    + <https://github.com/PyO3/setuptools-rust>  
  
---  
  
