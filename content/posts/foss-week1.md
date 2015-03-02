Title: FOSS week1
Slug: foss-week1
Date: 2015-03-02 12:57:15
Authors: m157q
Category: Course
Tags: Course, FOSS, Note
Summary: A note for 2015 FOSS course in NCTU, Hsinchu, Taiwan

+ Android Bionic
    + <https://github.com/android/platform_bionic>
    + <http://en.wikipedia.org/wiki/Bionic_(software)>

---

### How A Compiler Works

<http://www.slideshare.net/jserv/how-a-compiler-works-gnu-toolchain>

+ 1985 Richard Stallman GUN FSF
+ 屠龍書 - Syntax Directed Translator (SDT)
+ Embedded System - Toolchain 太新或太舊都不行
+ 第一版 gcc 是 RMS 寫的，之後的版本漸漸偏離 RMS 的初衷 
+ Dead Code Elimination
+ Code Motion, Loop invariant, Pointer Aliasing 
    + Pointer Aliasing 是 Compiler 最佳化瓶頸之一，如果不同的 Pointer 指向同個 address，會造成某些generic 的最佳化出錯
    + C99, Restrict Pointer Aliasing
        + [Pointer aliasing - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Pointer_aliasing)
        + In C99, the restrict keyword was added, which specifies that a pointer argument does not alias any other pointer argument.
+ Static Single Assignment (SSA)
+ cc1: 真正的 GNU C Compiler
    + Source Code
    + Simplified AST
    + Gimple IR
    + Tree SSA Form
    + RTL IR (LISP Style)
    + Final SAM
+ Pipeline Scheduling
    + <http://en.wikipedia.org/wiki/Classic_RISC_pipeline>
    + Instruction Fetch, Decode, Execute, Memory Access, Write Back
    + [Hazard (computer architecture) - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Hazard_%28computer_architecture%29)
+ LLVM
    + UIUC Vikram Adve, Chris Lattner in 2000
    + 高度模組化
    + LLVM bitcode (IR)
    + LLVM 一開始是用 GCC 的 Front-end (GPLv2)，但後來 RMS 在 gcc43 時將授權改為 GPLv3 來反對 LLVM 這種偷幹 Front-end 的方式，導致後來 Apple 發展自己的 Front-end Clang
    + Clang 採模組化設計 (Clang C API)
        + 可 export AST
        + 改善錯誤訊息
    + LLVM Bitcode 用來當傳遞格式還有很多問題
        + Binary Compatibility
    + 目前效能已經逼近 GCC 但還差一點

+ Objective-C
    + 1988
    + Steve Jobs
    + NeXT
    + GCC 2.7

在 Open Source 圈中，誠信是很重要的，千萬別幹抄襲這種事。

---

### Revolution OS

+ [從 Revolution OS 看作業系統生態變化 - fossapc.hackpad.com](https://fossapc.hackpad.com/-Revolution-OS--RrJpYEByzmr)
+ [Revolution OS - Wikipedia, the free encyclopedia](http://en.wikipedia.org/wiki/Revolution_OS)
+ [Revolution OS - YouTube](https://www.youtube.com/watch?v=jw8K460vx1c)
+ 影片裡同時出現了 RMS 和 Linus，可能以後都不會再看到他們同時出現在同個地方了。
    + RMS 是非常純的自由教義派，可以為了 Open Source BIOS 去用[龍芯](http://zh.wikipedia.org/zh-tw/%E9%BE%99%E8%8A%AF)    
    + Linus 則是實用主義派，可以為了實用而向沒有 Open Source 妥協，這是 RMS 完全沒辦法接受的。
    
GNU 早期最知名的軟體就是 Emacs  
    
MicroSoft NBC 在 Linux 被大量採用的年代很多頭條都是跟 Linux 有關的，形成一股趣味的對比。ex: VA Linux
紅到連賣大同電鍋的大同公司當年都搞了一套叫做 MITUX 的 UNIX 系統。  
    
GNU Mach 影響了 OS X 10.x 和 Windows NT
